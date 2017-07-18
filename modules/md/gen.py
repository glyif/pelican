#!/usr/bin/env python3


import sys
from .decors import *
from ..langs import *
from ..xml import ReadmeXMLReader, TextTag, TextGroupTag
from functools import partial


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

        # Read input
        self.xml = ReadmeXMLReader(infile)

        # Load parser
        parser = self.__load_parser(lang=language)
        if any_ext is True and parser is parse:
            raise ValueError('Any file extensions requires specifying a specific language')

        if parser is parse:
            self.parser = parser
        else:
            self.parser = partial(parser, any_ext=any_ext)

        # Other properties
        self.parsed = ''
        self.lang = language
        self.mdfile = outfile
        self.dir = workdir

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
