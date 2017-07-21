#!/usr/bin/env python3


import sys
from .c import C
from .js import JavaScript
from .python import Python
from .base import LANGUAGE_EXTENSIONS
from helpers import isfile, getext

__all__ = ['parse']


def parse(fpath):
    """
    Routes what parser to use depending on the file extension of a file

    :param fpath: file path of file
    :return: none
    """
    # Check existence
    if not isfile(fpath):
        raise FileNotFoundError('File is not existed')

    # Get file extension
    ext = getext(fpath)

    # Get module
    parser = None
    for lang, exts in LANGUAGE_EXTENSIONS.items():
        if ext in exts:
            parser = getattr(sys.modules[__name__], lang)
            break

    # If extension is not found
    if parser is None:
        raise FileExistsError('File extension is not supported')

    # Parse and return
    return parser(fpath)
