#!/usr/bin/env python3

import os, sys
from .c import C
from .js import JavaScript
from .python import Python
from config import C_EXTENSIONS, PYTHON_EXTENSIONS, JAVASCRIPT_EXTENSIONS

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
    if not os.path.isfile(fpath):
        raise FileNotFoundError('File is not existed: %s' % fpath)

    # Get file extension
    _, ext = os.path.splitext(fpath)

    # Get module
    cls = None
    for lang, exts in MAPPING.items():
        if ext in exts:
            cls = getattr(sys.modules[__name__], lang)
            break

    # If extension is not found
    if cls is None:
        raise ModuleNotFoundError('File extension is not supported: %s' % fpath)

    # Parse and return
    return cls(fpath)
