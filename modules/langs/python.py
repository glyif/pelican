#!/usr/bin/env python3

import re
from collections import OrderedDict

from helpers import count_indent
from .base import Base

__all__ = ['Python']

REGEX = {

    # Main regex for parsing Python structure
    'main': [
        re.compile(
            r'([ \t]*)((class|def)[ \t]+(\w+)[ \t]*(\([^:]*\))?[ \t]*:)\s+(("{3}|\'{3})(.*?(?="{3}|\'{3}))("{3}|\'{3}))?',
            flags=re.DOTALL
        )
    ],

    # Check regex for detecting docstring format being used
    'check': OrderedDict([

        # Google format
        (
            'google', [
                re.compile(r'\s*(Args|Returns|Raises):\s+')
            ]
        ),

        # Epytext format
        (
            'epytext', [
                re.compile(r'@(param|type|return|rtype|raise)[^@:\n]*:')
            ]
        ),

        # reStructuredText format
        (
            'rest', [
                re.compile(r':(param|returns|raises)[^:\n]*:')
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

        # Google format
        'google': {

            # Parsing Intro text part
            'intro': [
                re.compile(r'(.*?(?=Args:|Returns:|Raises:)|.*)', flags=re.DOTALL)
            ],

            # Parsing Arguments part
            'args': [
                re.compile(r'(?<=Args:)(.*?(?=Returns:|Raises:)|.*)', flags=re.DOTALL)
            ],

            # Parsing Returns part
            'returns': [
                re.compile(r'(?<=Returns:)(.*?(?=Raises:)|.*)', flags=re.DOTALL)
            ],

            # Parsing Raises part
            'raises': [
                re.compile(r'(?<=Raises:).*', flags=re.DOTALL)
            ],

            # Parsing key-value pairs if being used in part
            'kval': [
                re.compile(r'([^:\n]+):(?!/{2})(.*?(?=[^:\n]+:(?!/{2}))|.*)', flags=re.DOTALL),
                re.compile(r'()(.+)', flags=re.DOTALL)
            ]
        },

        # reStructuredText format
        'rest': {

            # Parsing Intro text part
            'intro': [
                re.compile(r'(.*?(?=:param|:return|:raise)|.*)', flags=re.DOTALL),
            ],

            # Parsing Arguments part
            'args': [
                re.compile(r':param(.*?(?=:return|:raise)|.*)', flags=re.DOTALL)
            ],

            # Parsing Returns part
            'returns': [
                re.compile(r':return(.*?(?=:raise)|.*)', flags=re.DOTALL)
            ],

            # Parsing Raises part
            'raises': [
                re.compile(r':raise.*', flags=re.DOTALL)
            ],

            # Parsing key-value pairs if being used in part
            'kval': [
                re.compile(r':\w+([^:\n]*):(.*?(?=:\w+[^:\n]*:)|.*)', flags=re.DOTALL)
            ]
        },

        # Epytext format
        'epytext': {

            # Parsing Intro text part
            'intro': [
                re.compile(r'(.*?(?=@param|@type|@rtype|@return|@raise)|.*)', flags=re.DOTALL)
            ],

            # Parsing Arguments part
            'args': [
                re.compile(r'@(?=param|type)(.*?(?=@return|@rtype|@raise)|.*)', flags=re.DOTALL)
            ],

            # Parsing Returns part
            'returns': [
                re.compile(r'@(?=return|rtype)(.*?(?=@raise)|.*)', flags=re.DOTALL)
            ],

            # Parsing Raises part
            'raises': [
                re.compile(r'@(?=raise).*', flags=re.DOTALL)
            ],

            # Parsing key-value pairs if being used in part
            'kval': [
                re.compile(r'@\w+([^@:\n]*):(.*?(?=@\w+[^@:\n]*:)|.*)', flags=re.DOTALL)
            ]
        }
    }
}


class Python(Base):
    """
    Python language file parser
    """

    def __init__(self, fpath, any_ext=False):
        """
        Initialize Python object

        :param fpath: file path
        :param any_ext: True means Parse source code files for any file extensions
        """
        self.typemap = {'class': 'Class', 'def': 'Function'}
        super(Python, self).__init__(
            fpath=fpath,
            lang=self.__class__.__name__,
            regex=REGEX,
            any_ext=any_ext
        )

    def parse(self):
        """
        Parse python file and create nodes with documentation info

        :return: none
        """
        previous = None
        cur_parents = []
        cur_indents = []
        for index, found in enumerate(self.founds):
            # Parse node
            name = found[3]
            type_ = self.typemap[found[2]]
            prototype = found[1]
            docstring = found[7]
            try:
                indent = count_indent(found[0], tab_to_spaces=4)
            except ValueError as msg:
                raise IndentationError('{:s}, at "{:s}"'.format(msg, prototype))

            # For first node
            if previous is None:
                self.add_node(index, name, type_, prototype, docstring)
                previous = index
                cur_indents.append(indent)
                continue

            # For new child
            if indent > cur_indents[-1]:
                if indent - cur_indents[-1] > 1:
                    raise IndentationError('Too much indents used, at "{:s}"'.format(prototype))
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
            kwargs = {'ischild': len(cur_parents) > 0, 'parent_list': cur_parents}
            self.add_node(index, name, type_, prototype, docstring, **kwargs)

            # Keep previous
            previous = index
