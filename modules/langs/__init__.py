#!/usr/bin/env python3


from .base import ALL_LANGUAGES, KeyValue
from .c import C
from .js import JavaScript
from .parser import parse
from .python import Python

__all__ = [
    'C',
    'JavaScript',
    'Python',
    'parse',
    'ALL_LANGUAGES',
    'KeyValue'
]
