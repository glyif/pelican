#!/usr/bin/env python3


__all__ = [
    'md_code',
    'md_header',
    'md_image',
    'md_inline',
    'md_bullet',
    'md_link',
    'md_quote',
    'md_bold',
    'md_italic',
    'md_paragraph',
    'md_escape'
]


def md_image(alt, url):
    return '![{}]({})'.format(alt, url) if alt or url else ''


def md_header(text, size):
    if not text:
        return ''
    l = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    size = l.index(size) + 1 if size in l else 0
    return '{} {}'.format('#' * size, text) if size else text


def md_code(code, lang=''):
    return '```{}\n{}\n```'.format(lang, code) if code else ''


def md_inline(code):
    return '`{}`'.format(code) if code else ''


def md_quote(text):
    return '> {}'.format(text) if text else ''


def md_link(text, url):
    return '[{}]({})'.format(text, url) if text or url else ''


def md_bullet(text, indent=1):
    return '{} {}'.format('-' * indent, text) if text else ''


def md_bold(text):
    return '**{}**'.format(text) if text else ''


def md_italic(text):
    return '*{}*'.format(text) if text else ''


def md_paragraph(header, hsize, text):
    return '{}{}'.format(
        '%s\n' % md_header(header, hsize) if header else '',
        text if text else ''
    )

def md_escape(word):
    for c in '_*`':
        for l in [3, 2, 1]:
            p = c * l
            if word.startswith(p) and word.endswith(p):
                e = '\%s' % c * l
                return '{e}{w}{e}'.format(e=e, w=word[l:len(word)-l])
    return word
