#!/usr/bin/env python3


from .c import C
from .js import JavaScript
from .python import Python
from .parser import parse
from .base import ALL_LANGUAGES, KeyValue

__all__ = [
    'C',
    'JavaScript',
    'Python',
    'parse',
    'ALL_LANGUAGES',
    'KeyValue'
]
