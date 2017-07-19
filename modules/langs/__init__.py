#!/usr/bin/env python3


from .c import C
from .js import JavaScript
from .python import Python, KeyValue
from .parser import parse, ALL_LANGUAGES

__all__ = [
    'C',
    'JavaScript',
    'Python',
    'parse',
    'ALL_LANGUAGES',
    'KeyValue'
]
