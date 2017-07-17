#!/usr/bin/env python3

import re
from collections import OrderedDict, namedtuple
from helpers import readfile, find_matches, getext
from config import PYTHON_EXTENSIONS

KeyValue = namedtuple('KeyValue', 'key val')

REGEX = {

    # Main regex for parsing Python structure
    'main': [ ],

    # Check regex for detecting docstring format being used
    'check': OrderedDict([

        # Google format
        (
            'google', [
                #re.compile()
                ]
        ),

        # Epytext format
        (
            'epytext', [
                #re.compile()
                ]
        ),

        # reStructuredText format
        (
            'rest', [
                #re.compile()
                ]
        ),

        # Unknown format
        (
            'unknown', [
                #re.compile()
                ]
        )
    ]),

    # Doc regex for parsing docstring
    'doc': {

        # Google format
        'google': {

            # Parsing Intro text part
            'intro': [
                #re.compile()
                ],

            # Parsing Arguments part
            'args': [
                #re.compile()
                ],

            # Parsing Returns part
            'returns': [
                #re.compile()
                ],

            # Parsing Raises part
            'raises': [
                #re.compile()
                ],

            # Parsing key-value pairs if being used in part
            'kval': [
                #re.compile()
                ]
        },

        # reStructuredText format
        'rest': {

            # Parsing Intro text part
            'intro': [
                #re.compile()
                ],

            # Parsing Arguments part
            'args': [
                #re.compile()
                ],

            # Parsing Returns part
            'returns': [
                #re.compile()
                ],

            # Parsing Raises part
            'raises': [
                #re.compile()
                ],

            # Parsing key-value pairs if being used in part
            'kval': [
                #re.compile()
                ]
        },

        # Epytext format
        'epytext': {

            # Parsing Intro text part
            'intro': [
                #re.compile()
                ],

            # Parsing Arguments part
            'args': [
                #re.compile()
                ],

            # Parsing Returns part
            'returns': [
                #re.compile()
                ],

            # Parsing Raises part
            'raises': [
                #re.compile()
                ],

            # Parsing key-value pairs if being used in part
            'kval': [
                #re.compile()
                ]
        }
    }
}


class Python:

    def __init__(self, fpath, any_ext=False):
        # Check file extension
        if not any_ext:
            ext = getext(fpath)
            if ext not in PYTHON_EXTENSIONS:
                raise ValueError('File extension is not supported')

        # Check file content
        self.content = readfile(fpath)
        if self.content.strip() == '':
            raise FileExistsError('File is empty')

        # Define self language
        self.lang = self.__class__.__name__.lower()

        # Parse file
        self.nodes = OrderedDict()
        self.founds = find_matches(self.content, REGEX['main'])
        if self.founds:
            self.__parse()

    @staticmethod
    def __count_indent(indent, tab_to_spaces=4):
        # No indent
        if indent == '':
            return 0
        # Inconsistent indent
        if len(set(indent)) > 1:
            raise IndentationError('Too many indents found')
        # Indent is space
        if ' ' in indent:
            if len(indent) % tab_to_spaces != 0:
                raise IndentationError('Indent used is not standard')
            return int(len(indent) / tab_to_spaces)
        # Indent is tab
        elif '\t' in indent:
            return len(indent)
        # Unsupported indent
        else:
            raise IndentationError('Unsupported indent')

    @staticmethod
    def __gen_node(prototype, docstring):
        return {
            'prototype': prototype,
            'document': Python.__parse_doc(docstring),
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

    @staticmethod
    def __parse_doc(docstring):
        ret = {
            'intro': None,
            'args': None,
            'returns': None,
            'raises': None
        }
        for style, regex in REGEX['check'].items():
            # Check style
            matched = find_matches(docstring, regex)
            if matched:
                # Unknown style
                if style == 'unknown':
                    ret['intro'] = matched[0].strip()
                # Known style
                else:
                    regex = REGEX['doc'][style]
                    ret['intro'] = Python.__doc_extract(docstring, regex['intro'])
                    ret['args'] = Python.__doc_extract(docstring, regex['args'], kval=regex['kval'])
                    ret['returns'] = Python.__doc_extract(docstring, regex['returns'], kval=regex['kval'])
                    ret['raises'] = Python.__doc_extract(docstring, regex['raises'], kval=regex['kval'])
                break
        return ret

    def __get_childs(self, childs, index):
        return self.nodes[index]['childs'] if childs is None else childs[index]['childs']

    def __store_child(self, index, node, parents):
        childs = None
        for parent in parents:
            childs = self.__get_childs(childs, parent)
        childs[index] = node

    def __parse(self):
        previous = None
        cur_parents = []
        cur_indents = []
        for index, found in enumerate(self.founds):
            # Parse node
            indent = self.__count_indent(found[0])
            prototype = found[1]
            docstring = found[6]
            node = self.__gen_node(prototype, docstring)

            # For first node
            if previous is None:
                self.nodes[index] = node
                previous = index
                cur_indents.append(indent)
                continue

            # For new child
            if indent > cur_indents[-1]:
                if indent - cur_indents[-1] > 1:
                    raise IndentationError('Bad indent at "{:s}"'.format(prototype))
                cur_parents.append(previous)  # add parent
                cur_indents.append(indent)  # add indent

            # For child exit
            elif indent < cur_indents[-1]:
                left = cur_indents.index(indent)
                right = cur_indents.index(cur_indents[-1])
                for _ in range(right - left):
                    cur_parents.pop(-1)  # remove parent
                    cur_indents.pop(-1)  # remove indent

            # Store node
            if len(cur_parents) > 0:
                self.__store_child(index, node, cur_parents)
            else:
                self.nodes[index] = node

            # Keep previous
            previous = index
