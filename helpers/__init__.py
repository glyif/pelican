#!/usr/bin/env python3

import os


def readfile(fpath):
    if not os.path.isfile(fpath):
        raise FileNotFoundError('File %s could not be found' % fpath)
    with open(fpath, 'r') as f:
        content = f.read()
    return content


def find_matches(text, patterns):
    patterns = [patterns] if isinstance(patterns, str) else list(patterns)
    for pattern in patterns:
        found = pattern.findall(text)
        if found:
            return found
    return []
