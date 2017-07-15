#/usr/bin/env python3

from xml.dom.minidom import Element, Text, parse
from xml.parsers.expat import ExpatError
from collections import namedtuple

TextTag = namedtuple('TextTag', 'name text atts')
TextGroupTag = namedtuple('TextGroupTag', 'name tags atts')


class XMLReader:

    def __init__(self, fpath):

        # Parse XML
        try:
            self.dom = parse(fpath).documentElement
        except FileNotFoundError:
            raise FileNotFoundError('Unable to find XML file: {:s}'.format(fpath))
        except ExpatError:
            raise FileExistsError('Unable to read XML file: {:s}'.format(fpath))

        # Document root element attributes
        self.name = self.dom.tagName
        self.atts = self.atts_in_tag(self.dom)

    @staticmethod
    def is_text(tag):
        return any([
            len(tag.childNodes) == 0 and tag.firstChild is None,
            len(tag.childNodes) == 1 and isinstance(tag.firstChild, Text)
        ])

    @staticmethod
    def is_textgroup(tag):
        ret = False  # init check result
        subs = tag.childNodes  # load sub-tags
        # Loop through sub-tags
        for sub in subs:
            # Sub-tag found
            if isinstance(sub, Element):
                # Return False if sub-tag is not text
                if not XMLReader.is_text(sub):
                    return False
                # Mark True if sub-tag is text
                ret = True
        # Return check result
        return ret

    @staticmethod
    def text_in_tag(tag):
        return '' if tag.firstChild is None else tag.firstChild.data.strip()

    @staticmethod
    def atts_in_tag(tag):
        return dict(tag.attributes.items())

    @staticmethod
    def read_tag(tag):

        # For text tag
        if XMLReader.is_text(tag):
            return TextTag(
                name = tag.tagName,
                text = XMLReader.text_in_tag(tag),
                atts = XMLReader.atts_in_tag(tag)
            )

        # For tag containing group of text tags
        elif XMLReader.is_textgroup(tag):

            # Read sub-tags in tag
            subs = [
                TextTag(
                    name = sub.tagName,
                    text = XMLReader.text_in_tag(sub),
                    atts = XMLReader.atts_in_tag(sub)
                )
                for sub in tag.childNodes if isinstance(sub, Element)
            ]

            # Return tag including its sub-tags
            return TextGroupTag(
                name = tag.tagName,
                tags = subs,
                atts = XMLReader.atts_in_tag(tag)
            )

        # For unknown tags
        else:
            raise NotImplementedError('Unsupported tag: <{:s}>'.format(tag.tagName))

    def get_tag(self, tagname):
        try:
            tag = self.dom.getElementsByTagName(tagname)[0]
            return self.read_tag(tag)  # tag found
        except IndexError:
            return None  # tag not found

    def get_tags(self, tagname):
        tags = self.dom.getElementsByTagName(tagname)
        return [self.read_tag(tag) for tag in tags]


class ReadmeXMLReader(XMLReader):

    def __init__(self, fpath):
        super(ReadmeXMLReader, self).__init__(fpath)

    @property
    def title(self):
        return self.get_tag('title')

    @property
    def author(self):
        return self.get_tag('author')

    @property
    def license(self):
        return self.get_tag('license')

    @property
    def files(self):
        return self.get_tag('files')