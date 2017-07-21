#!/usr/bin/env python3


from collections import namedtuple, OrderedDict
from helpers import readfile, find_matches, getext
from config import C_EXTENSIONS, PYTHON_EXTENSIONS, JAVASCRIPT_EXTENSIONS

__all__ = [
    'KeyValue',
    'LANGUAGE_EXTENSIONS',
    'ALL_LANGUAGES',
    'BaseLang'
]

# Key-value data structure
KeyValue = namedtuple('KeyValue', 'key val')

# Language extensions mapping
LANGUAGE_EXTENSIONS = {
    # Python file extensions
    'Python': PYTHON_EXTENSIONS,
    # Ansi-C file extentions
    'C': C_EXTENSIONS,
    # Javascript file extentions
    'JavaScript': JAVASCRIPT_EXTENSIONS
}

# All current supported languages
ALL_LANGUAGES = list(LANGUAGE_EXTENSIONS.keys())


class Base:
    """
    Base parser for all languages
    """

    def __init__(self, fpath, lang, regex, any_ext=False):
        """

        :param fpath:
        :param lang:
        :param regex:
        :param any_ext:
        """
        # Check lang input
        if lang not in LANGUAGE_EXTENSIONS:
            raise ValueError('Unrecognized input language "{:s}"'.format(lang))

        # Check file extension
        if not any_ext:
            ext = getext(fpath)
            if ext not in LANGUAGE_EXTENSIONS[lang]:
                raise FileExistsError('File extension is not supported')

        # Check file content
        self.content = readfile(fpath)
        if self.content.strip() == '':
            raise FileExistsError('File is empty')

        # Define self properties
        self.lang = lang.lower()
        self.regex = regex

        # Parse file
        self.nodes = OrderedDict()
        self.founds = find_matches(self.content, self.regex['main'])
        if self.founds:
            self.parse()

    def __gen_node(self, name, type_, prototype, docstring):
        return {
            'name': name,
            'type': type_,
            'prototype': prototype,
            'document': self.__parse_doc(docstring),
            'childs': OrderedDict()
        }

    @staticmethod
    def __doc_extract(docstring, patterns, kval=None):
        matched = find_matches(docstring, patterns)
        if matched and matched[0].strip() != '':
            ret = matched[0].strip()
            if kval is not None:
                matched = find_matches(ret, kval)
                if matched:
                    # Get key-value pairs
                    return [KeyValue(key=k.strip(), val=v.strip()) for k, v in matched]
            # Get text only
            return ret
        # No match found
        return None

    def __parse_doc(self, docstring):
        # Init doc structure
        ret = {
            'intro': None,
            'args': None,
            'returns': None,
            'raises': None
        }

        # Do parse
        for type_, regex in self.regex['check'].items():
            # Check style
            matched = find_matches(docstring, regex)
            if matched:
                # Unknown style
                if type_ == 'unknown':
                    ret['intro'] = matched[0].strip()
                # Known style
                else:
                    regex = self.regex['doc'][type_]
                    ret['intro'] = self.__doc_extract(docstring, regex['intro'])
                    ret['args'] = self.__doc_extract(docstring, regex['args'], kval=regex['kval'])
                    ret['returns'] = self.__doc_extract(docstring, regex['returns'], kval=regex['kval'])
                    ret['raises'] = self.__doc_extract(docstring, regex['raises'], kval=regex['kval'])
                break

        # Return parsed doc
        return ret

    def __get_childs(self, childs, index):
        return self.nodes[index]['childs'] if childs is None else childs[index]['childs']

    def __store_child(self, index, node, parents):
        childs = None
        for parent in parents:
            childs = self.__get_childs(childs, parent)
        childs[index] = node

    def add_node(self, index, name, type_, prototype, docstring, ischild=False, parent_list=None):
        if ischild and not parent_list:
            raise ValueError('"parent_list" is required to store child node')
        node = self.__gen_node(name=name, type_=type_, prototype=prototype, docstring=docstring)
        if ischild:
            self.__store_child(index=index, node=node, parents=parent_list)
        else:
            self.nodes[index] = node

    def parse(self):
        pass