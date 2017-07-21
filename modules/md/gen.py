#!/usr/bin/env python3

import sys
from config import *
from .decors import *
from ..langs import *
from ..xml import ReadmeXMLReader
from helpers import writefile, allfiles, pathprep, basedir, whoami
from functools import partial

__all__ = ['MDGen']

PARTSEP = '\n\n'


class MDGen:

    def __init__(self, infile, outfile, workdir, language=None, any_ext=False):
        """
        Initialize MDGen object

        :param infile:    Specify XML file as input
        :param outfile:   Specify output filename for writing result
        :param workdir:   Directory containing source code to be scanned if being required
        :param language:  Programming language used in source code
        :param any_ext:   True means Parse source code files in any file extensions
        """

        # Read input as definitions
        self.defs = ReadmeXMLReader(infile)

        # Load parser
        parser = self.__load_parser(lang=language)
        if any_ext is True and parser is parse:
            # General parser does not work with any file extensions
            raise ValueError('Any file extensions requires specifying a specific language')
        self.parser = parser if parser is parse else partial(parser, any_ext=any_ext)

        # Other properties
        self.parts = {}
        self.pool = []
        self.content = ''
        self.mdfile = outfile
        self.wdir = workdir
        self.order = 0
        self.scanned = False

        # Do tasks
        self.__generate()
        self.__textize()
        self.__write_md()

    @property
    def next_order(self):
        """Increase order and return when being called"""
        self.order += 1
        return self.order

    @staticmethod
    def __load_parser(lang):
        # Get current module
        this = sys.modules[__name__]

        # Load general parser if not specified
        if lang is None:
            return getattr(this, 'parse')

        # Load specific parser if specified
        lang = str(lang)
        for item in ALL_LANGUAGES:
            if item.lower() == lang.lower():
                return getattr(this, item)

        # Parser not found
        raise ValueError('Language is not supported: {:s}'.format(lang))

    @classmethod
    def __kv_decor(cls, key, val, isparam=False):
        sign = '@' if AT_SIGN_BEFORE_PARAM is True and isparam else ''
        val = cls.__merge_lines(val)
        line = '{} {}'.format(md_inline(sign + key), val) if key else val
        return md_bullet(line)

    @classmethod
    def __gen_keyval(cls, pairs, header, isparam=False):
        txt = '\n'.join(cls.__kv_decor(k, v, isparam) for k, v in pairs)
        return md_paragraph(header, PROTOTYPE_PARTS_HSIZE, txt)

    @staticmethod
    def __merge_lines(text):
        return ' '.join(line.strip() for line in text.split('\n'))

    def __textize(self):
        # Unpack generated parts in order
        _, parts = zip(*sorted(self.parts.items()))
        # Store parts in text
        self.content = PARTSEP.join(parts)

    def __write_md(self):
        writefile(
            fpath=self.mdfile,
            content=self.content,
            overwrite=True
        )

    def __generate(self):
        self.__gen_logo()
        self.__gen_title()
        self.__gen_author()
        self.__gen_paragraphs()
        self.__gen_files()
        self.__gen_license()

    def __gen_logo(self):
        # Check availability
        if self.defs.logo is None:
            return

        # Load logo settings
        logo = self.defs.logo
        alt = logo.atts.get('alt', DEFAULT_LOGO_ALT)
        url = logo.atts.get('src', DEFAULT_LOGO_URL)

        # Generate logo content
        text = md_image(alt=alt, url=url)

        # Store logo content
        if text:
            self.parts[logo.index] = text

    def __gen_title(self):
        # Check availability
        if self.defs.title is None:
            return

        # Load title settings
        title = self.defs.title
        hsize = title.atts.get('hsize', DEFAULT_TITLE_HSIZE)

        # Generate title content
        text = md_header(
            text='{}'.format(title.text if title.text else basedir(self.wdir)),
            size=hsize
        )

        # Store title content
        if text:
            self.parts[title.index] = text

    def __gen_author(self):
        # Check availability
        if self.defs.author is None:
            return

        # Load author settings
        author = self.defs.author
        hsize = author.atts.get('hsize', DEFAULT_AUTHOR_HSIZE)
        prefix = author.atts.get('prefix', DEFAULT_AUTHOR_PREFIX)
        suffix = author.atts.get('suffix', DEFAULT_AUTHOR_SUFFIX)

        # Generate author content
        text = md_header(
            text='{}{}{}'.format(
                '%s ' % prefix if prefix else '',
                author.text if author.text else whoami(),
                ' %s' % suffix if suffix else ''
            ),
            size=hsize
        )

        # Store author content
        if text:
            self.parts[author.index] = text

    def __gen_paragraphs(self):
        # Check availability
        if not self.defs.paragraphs:
            return

        # Loop through each paragraph
        for p in self.defs.paragraphs:

            # Load paragraph settings
            header = p.atts.get('header', '')
            hsize = p.atts.get('hsize', DEFAULT_PARAGRAPH_HSIZE)

            # Generate paragraph content
            text = md_paragraph(header, hsize, p.text)

            # Store paragraph content
            if text:
                self.parts[p.index] = text

    def __gen_license(self):
        # Check availability
        if self.defs.license is None:
            return

        # Load license settings
        lic = self.defs.license
        header = lic.atts.get('header', DEFAULT_LICENSE_HEADER)
        hsize = lic.atts.get('hsize', DEFAULT_LICENSE_HSIZE)
        type_ = lic.atts.get('type', DEFAULT_LICENSE_TYPE)

        # Generate license content
        text = md_paragraph(
            header=header,
            hsize=hsize,
            text='{}{}'.format(
                '%s\n' % type_ if type_ else '',
                lic.text if lic.text else ''
            )
        )

        # Store license content
        if text:
            self.parts[lic.index] = text

    def __gen_files(self):
        # Check availability
        if self.defs.files is None:
            return

        files = self.defs.files

        # Generate header for file group
        header = files.atts.get('header', DEFAULT_FILES_HEADER)
        hsize = files.atts.get('hsize', DEFAULT_FILES_HSIZE)
        text = md_header(text=header, size=hsize)
        if text:
            self.pool.append(text)

        # Prepare file item settings
        fpath_hsize = files.atts.get('fpath_hsize', DEFAULT_FILEPATH_HSIZE)
        fpath_order = files.atts.get('fpath_order', USE_NUM_BEFORE_FILEPATH)
        if isinstance(fpath_order, str):
            convert = lambda val: True if val.lower() == 'yes' else False
            fpath_order = convert(fpath_order)
        kwargs = {
            'fpath_hsize': fpath_hsize,
            'fpath_order': fpath_order
        }

        # Generate file items
        for tag in files.tags:
            self.__gen_a_file(tag, **kwargs)

        # Join generated data
        if len(self.pool) > 1:
            self.parts[files.index] = PARTSEP.join(self.pool)

    def __gen_a_file(self, tag, **kwargs):
        caption = tag.text
        fpath = tag.atts.get('path', '')

        # File tag without path
        if fpath == '':
            return

        # File tag with "*" as path value
        elif fpath == '*':
            self.__scan(caption=caption, **kwargs)

        # File tag with specific path
        else:
            self.__parse(fpath=fpath, caption=caption, **kwargs)

    def __scan(self, caption, **kwargs):
        # Quit if already scanned
        if self.scanned is True:
            return

        # Traverse files in working dir
        for fpath in allfiles(self.wdir, SKIP_LEADING_DOT_ITEMS_IN_FOLDER):
            self.__parse(fpath=fpath, caption=caption, **kwargs)

        # Mark as already scanned
        self.scanned = True

    def __parse(self, fpath, caption, **kwargs):
        # Prepare file path
        abs_path, rel_path = pathprep(self.wdir, fpath)

        # Check file path
        if abs_path is None:
            print('Skipped:', fpath, '- File and working dir are not related')
            return

        # Parse file
        try:
            parsed = self.parser(fpath)
            # No parsed data found
            if not parsed.nodes:
                print('Skipped:', fpath, '- No data to generate')
                return
        except Exception as msg:
            print('Skipped:', fpath, '-', msg)
            return

        # Generate first paragraph for file item
        use_order = kwargs.get('fpath_order')
        hsize = kwargs.get('fpath_hsize')
        header = '%s - %s' % (self.next_order, rel_path) if use_order else rel_path
        self.pool.append(md_paragraph(header, hsize, caption))

        # Process parsed data
        lang = parsed.lang
        for node in parsed.nodes.values():
            self.__parse_node(node=node, lang=lang)

        # Output result
        print('Parsed:', fpath)

    def __parse_node(self, node, lang, parent=None):
        # Generate function name
        name = node['name']
        type_ = node['type']
        self.pool.append(
            md_header(
                text='{}{}'.format(
                    '%s: ' % type_.capitalize() if DISPLAY_TYPE_BEFORE_PROTOTYPE_NAME is True else '',
                    md_escape(name)
                ),
                size=DEFAULT_PROTOTYPE_SECTION_HSIZE
            )
        )

        # Generate function prototype
        ptype = node['prototype']
        if parent is not None:
            indent = max(s.count('\t') for s in parent.split('\n')) + 1
            ptype = '%s\n%s%s' % (parent, '\t' * indent, ptype)
        self.pool.append(md_code(ptype, lang))

        # Generate function intro
        intro = node['document']['intro']
        if intro is not None:
            self.pool.append(self.__merge_lines(intro))

        # Generate function params
        params = node['document']['args']
        if params is not None:
            self.pool.append(
                self.__gen_keyval(params, PROTOTYPE_PARAMS_HEADER, isparam=True)
            )

        # Generate function returns
        returns = node['document']['returns']
        if returns is not None:
            self.pool.append(
                self.__gen_keyval(returns, PROTOTYPE_RETURNS_HEADER)
            )

        # Generate function raises
        raises = node['document']['raises']
        if raises is not None:
            self.pool.append(
                self.__gen_keyval(raises, PROTOTYPE_RAISES_HEADER)
            )

        # Generate child nodes if any
        childs = node['childs']
        if childs:
            for child in childs.values():
                self.__parse_node(node=child, lang=lang, parent=ptype)