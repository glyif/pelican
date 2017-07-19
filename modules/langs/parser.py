#!/usr/bin/env python3

import sys
from .c import C
from .js import JavaScript
from .python import Python
from helpers import isfile, getext
from config import C_EXTENSIONS, PYTHON_EXTENSIONS, JAVASCRIPT_EXTENSIONS

__all__ = ['parse', 'ALL_LANGUAGES']

MAPPING = {

    # Python file extensions
    'Python': PYTHON_EXTENSIONS,

    # Ansi-C file extentions
    'C': C_EXTENSIONS,

    # Javascript file extentions
    'JavaScript': JAVASCRIPT_EXTENSIONS

}

ALL_LANGUAGES = list(MAPPING.keys())


def parse(fpath):
    # Check existence
    if not isfile(fpath):
        raise FileNotFoundError('File is not existed')

    # Get file extension
    ext = getext(fpath)

    # Get module
    parser = None
    for lang, exts in MAPPING.items():
        if ext in exts:
            parser = getattr(sys.modules[__name__], lang)
            break

    # If extension is not found
    if parser is None:
        raise ModuleNotFoundError('File extension is not supported')

    # Parse and return
    return parser(fpath)
