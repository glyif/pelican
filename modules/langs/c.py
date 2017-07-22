#!/usr/bin/env python3


import re
from collections import OrderedDict
from .base import Base

__all__ = ['C']

REGEX = {

    # Main regex for parsing C structure
    'main': [
        re.compile(r'(/\*([^/]|[^*]/[^*])*\*/\s*)?((\w+(?<!else) +)+(\*? *\w+) *\([^()]*\))\s*{', flags=re.DOTALL)
    ],

    # Check regex for detecting docstring format being used
    'check': OrderedDict([

        # JSDoc format for C
        (
            'jsdoc', [
                re.compile(r'@(param|returns?|throws?)[ \t]*([[{].*[]}])?')
            ]
        ),

        # Betty format
        (
            'betty', [
                re.compile(r'(@\*{0,2}\w+|[Rr]eturns?)[ \t]*:.*?')
            ]
        ),

        # Unknown format
        (
            'unknown', [
                re.compile(r'.+', flags=re.DOTALL)
            ]
        )
    ]),

    # Doc regex for parsing docstring
    'doc': {

        # JSDoc format for C
        'jsdoc': {

            # Parsing Intro text part
            'intro': [
                re.compile(r'(.*?(?=@param|@returns?|@throws?)|.*)', flags=re.DOTALL)
            ],

            # Parsing Arguments part
            'args': [
                re.compile(r'@param(.*?(?=@returns?|@throws?)|.*)', flags=re.DOTALL)
            ],

            # Parsing Returns part
            'returns': [
                re.compile(r'@returns?(.*?(?=@throws?)|.*)', flags=re.DOTALL)
            ],

            # Parsing Raises part
            'raises': [
                re.compile(r'@throws?.*', flags=re.DOTALL)
            ],

            # Parsing key-value pairs if being used in part
            'kval': [
                re.compile(
                    r'@param[ \t]*([[{][^][@}{]+[]}][ \t]+\*{0,2}\w+|\*{0,2}\w+)[ \t-]*(.*?(?=@param)|.*)',
                    flags=re.DOTALL
                ),
                re.compile(r'@\w+[ \t]*([[{][^][@}{]+[]}])?[ \t-]*(.*?(?=@\w+)|.*)', flags=re.DOTALL)
            ]
        },

        # Betty format
        'betty': {

            # Parsing Intro text part
            'intro': [
                re.compile(r'(.*?(?=@\*{0,2}\w+[ \t]*:|[Rr]eturns?[ \t]*:)|.*)', flags=re.DOTALL)
            ],

            # Parsing Arguments part
            'args': [
                re.compile(r'@\*{0,2}\w+[ \t]*:.*?(?=[Rr]eturns?[ \t]*:)', flags=re.DOTALL),
                re.compile(r'@\*{0,2}\w+[ \t]*:.*', flags=re.DOTALL)
            ],

            # Parsing Returns part
            'returns': [
                re.compile(r'[Rr]eturns?[ \t]*:.*', flags=re.DOTALL)
            ],

            # No Raises part used, no document found
            'raises': [
                re.compile(r'^$', flags=re.DOTALL)
            ],

            # Parsing key-value pairs if being used in part
            'kval': [
                re.compile(r'(?<=@)([^:\n]+):(.*?(?=@)|.*)', flags=re.DOTALL),
                re.compile(r'(?<=[Rr]eturns)([^:\n]*):(.*)', flags=re.DOTALL),
                re.compile(r'(?<=[Rr]eturn)([^:\n]*):(.*)', flags=re.DOTALL)
            ]
        }
    }
}


class C(Base):
    """
    C language file parser
    """
    def __init__(self, fpath, any_ext=False):
        """
        Initializes C object

        :param fpath: path to c file
        :param any_ext: True means Parse source code files for any file extensions
        """

        super(C, self).__init__(
            fpath=fpath,
            lang=self.__class__.__name__,
            regex=REGEX,
            any_ext=any_ext
        )

    @staticmethod
    def __refine(doc):
        """
        gets rid of the * in front of the lines documentation lines

        :param doc: documentation line
        :return: regex string without "*"s
        """

        ret = re.sub(r'(/\*\*?|\*/)', r'', doc)
        ret = re.sub(r'(\n[ \t]*)(\*)', r'\1', ret)
        return ret

    def parse(self):
        """
        parses the c file and creates nodes of documentation

        :return: none
        """

        for index, found in enumerate(self.founds):
            # Parse node
            name = found[4]
            type_ = 'Function'
            prototype = found[2]
            docstring = self.__refine(found[0])
            self.add_node(index, name, type_, prototype, docstring)
