#!/usr/bin/env python3


def md_image(alt, url):
    return '![{}]({})'.format(alt, url)


def md_header(text, size):
    l = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    size = l.index(size) + 1 if size in l else 0
    return '{} {}'.format('#' * size, text) if size else text


def md_code(code, lang=''):
    return '```{}\n{}\n```'.format(lang, code)


def md_inline(code):
    return '`{}`'.format(code)


def md_quote(text):
    return '> {}'.format(text)


def md_link(text, url):
    return '[{}]({})'.format(text, url)
