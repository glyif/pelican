#!/usr/bin/env python3


from collections import namedtuple, OrderedDict

from config import C_EXTENSIONS, PYTHON_EXTENSIONS, JAVASCRIPT_EXTENSIONS
from helpers import readfile, find_matches, getext

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
        Initializes Base object

        :param fpath: file path of file
        :param lang: language of file
        :param regex: regex statments to parse
        :param any_ext: True means Parse source code files for any file extensions
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
        """
        generates a node

        :param name: name of the documentation (function/struct/class/etc)
        :param type_: type of documentation (function/struct/class/etc)
        :param prototype: prototype
        :param docstring: documentation
        :return:
        """

        return {
            'name': name,
            'type': type_,
            'prototype': prototype,
            'document': self.__parse_doc(docstring),
            'childs': OrderedDict()
        }

    @staticmethod
    def __doc_extract(docstring, patterns, kval=None):
        """
        extracts parts of docstring with regex

        :param docstring: full docsstring
        :param patterns: regex pattern
        :param kval: key and value pair
        :return: needed docstring text for __parse_doc
        """

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
        """
        parses docstring out into dictionary

        :param docstring: full docstring
        :return: parsed docstring in dictionary format
        """

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
        """
        get childs of a node

        :param childs: child
        :param index: index of child
        :return: child or None
        """
        return self.nodes[index]['childs'] if childs is None else childs[index]['childs']

    def __store_child(self, index, node, parents):
        """
        stores node as a child

        :param index: index of child
        :param node: node to add as child
        :param parents: parts of the child node
        :return: none
        """

        childs = None
        for parent in parents:
            childs = self.__get_childs(childs, parent)
        childs[index] = node

    def add_node(self, index, name, type_, prototype, docstring, ischild=False, parent_list=None):
        """
        adds a doc node

        :param index: index of node
        :param name: name of the function/struct/class/etc
        :param type_: type: function/struct/class/etc
        :param prototype: prototype of the function/struct/class/etc
        :param docstring: full docstring
        :param ischild: True if it is a child, default is false
        :param parent_list: parents of the node

        :return: none
        """
        if ischild and not parent_list:
            raise ValueError('"parent_list" is required to store child node')
        node = self.__gen_node(name=name, type_=type_, prototype=prototype, docstring=docstring)
        if ischild:
            self.__store_child(index=index, node=node, parents=parent_list)
        else:
            self.nodes[index] = node

    def parse(self):
        """
        empty parse function, will be overwritten by inherited parsers

        :return: none
        """

        pass
