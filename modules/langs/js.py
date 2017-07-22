#!/usr/bin/env python3


import re
from collections import OrderedDict

from .base import Base

__all__ = ['JavaScript']

REGEX = {

    # Main regex for parsing JS structure
    'main': [
        re.compile(r'(/\*([^/]|[^*]/[^*])*\*/\s*)?(function +(\w+) *\([^()]*\))\s*{', flags=re.DOTALL)
    ],

    # Check regex for detecting docstring format being used
    'check': OrderedDict([

        # JSDoc format
        (
            'jsdoc', [
                re.compile(r'@(param|returns?|throws?)[ \t]*([[{].*[]}])?')
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

        # JSDoc format
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
        }

    }
}


class JavaScript(Base):
    """
    Javascript language file parser
    """

    def __init__(self, fpath, any_ext=False):
        """
        Initializes Javascript object

        :param fpath: file path
        :param any_ext: True means Parse source code files for any file extensions
        """

        super(JavaScript, self).__init__(
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
        parses the js file and creates nodes of documentation

        :return: none
        """
        for index, found in enumerate(self.founds):
            # Parse node
            name = found[3]
            type_ = 'Function'
            prototype = found[2]
            docstring = self.__refine(found[0])
            self.add_node(index, name, type_, prototype, docstring)
