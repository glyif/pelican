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
    """
    wrapper for an md image

    :param alt: alt tag for the image
    :param url: url for the image
    :return: markdown for embedding an image
    """

    return '![{}]({})'.format(alt, url) if alt or url else ''


def md_header(text, size):
    """
    wrapper for md header text

    :param text: text in header
    :param size: text size (html)
    :return: md formatted header
    """

    if not text:
        return ''
    l = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    size = l.index(size) + 1 if size in l else 0
    return '{} {}'.format('#' * size, text) if size else text


def md_code(code, lang=''):
    """
    wrapper for md code block

    :param code: code inside of block
    :param lang: code language
    :return: md formatted code block
    """

    return '```{}\n{}\n```'.format(lang, code) if code else ''


def md_inline(code):
    """
    wrapper for md inline code phrase

    :param code: code
    :return: md formatted inline code phrase
    """

    return '`{}`'.format(code) if code else ''


def md_quote(text):
    """
    wrapper for md quotes

    :param text: text inside of quotes
    :return: md formatted quote block
    """

    return '> {}'.format(text) if text else ''


def md_link(text, url):
    """
    wrapper for md hyperlink

    :param text: text for link
    :param url: url for link
    :return: md formatted link
    """

    return '[{}]({})'.format(text, url) if text or url else ''


def md_bullet(text, indent=1):
    """
    wrapper for md bullet points

    :param text: text on bullet point
    :param indent: how much indent. default=1
    :return: md formatted bullet point
    """

    return '{} {}'.format('-' * indent, text) if text else ''


def md_bold(text):
    """
    wrapper for md bold text

    :param text: text to be bold
    :return: md formatted bold text
    """
    return '**{}**'.format(text) if text else ''


def md_italic(text):
    """
    wrapper for md italic text

    :param text: text to be italicized
    :return: md formatted italicized text
    """

    return '*{}*'.format(text) if text else ''


def md_paragraph(header, hsize, text):
    """
    wrapper for md text block

    :param header: header of text block
    :param hsize: size of header text block
    :param text: text of text block
    :return: md formatted text block with header
    """

    return '{}{}'.format(
        '%s\n' % md_header(header, hsize) if header else '',
        text if text else ''
    )

def md_escape(word):
    """
    wrapper for escaped characters

    :param word: escaped word
    :return: word
    """
    for c in '_*`':
        for l in [3, 2, 1]:
            p = c * l
            if word.startswith(p) and word.endswith(p):
                e = '\%s' % c * l
                return '{e}{w}{e}'.format(e=e, w=word[l:len(word)-l])
    return word
