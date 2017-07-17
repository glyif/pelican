#!/usr/bin/env python3

import os

def readfile(fpath):
    if not os.path.isfile(fpath):
        raise FileNotFoundError('File {:s} could not be found'.format(fpath))
    with open(fpath, 'r') as f:
        content = f.read()
    return content


def find_matches(text, patterns):
    if isinstance(patterns, str):
        patterns = patterns
    else:
        patterns = list(patterns)

    for pattern in patterns:
        found = pattern.findall(text)
        if found:
            return found
    return []


def isfile(path):
    return os.path.isfile(path)


def getext(fpath):
    """Get file extension"""
    _, ext = os.path.splitext(fpath)
    return ext
