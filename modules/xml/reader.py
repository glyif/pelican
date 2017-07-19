#/usr/bin/env python3

from xml.dom.minidom import Element, Text, parse
from xml.parsers.expat import ExpatError
from collections import namedtuple

__all__ = [
    'XMLReader',
    'ReadmeXMLReader',
    'TextTag',
    'TextGroupTag'
]

TextTag = namedtuple('TextTag', 'name text atts index')
TextGroupTag = namedtuple('TextGroupTag', 'name tags atts index')


class XMLReader:

    def __init__(self, fpath):

        # Parse XML
        try:
            self.dom = parse(fpath).documentElement
        except FileNotFoundError:
            raise FileNotFoundError('Unable to find XML file: {:s}'.format(fpath))
        except ExpatError:
            raise FileExistsError('Unable to read XML file: {:s}'.format(fpath))

        # Document root element attributes
        self.name = self.dom.tagName
        self.atts = self.__atts_in_tag(self.dom)
        self.childs = self.dom.childNodes

    @staticmethod
    def __is_text(tag):
        return any([
            len(tag.childNodes) == 0 and tag.firstChild is None,
            len(tag.childNodes) == 1 and isinstance(tag.firstChild, Text)
        ])

    @classmethod
    def __is_textgroup(cls, tag, child_name=None):
        ret = False  # init check result
        subs = tag.childNodes  # load sub-tags
        # Loop through sub-tags
        for sub in subs:
            # Sub-tag found
            if isinstance(sub, Element):
                # Return False if sub-tag is not text
                if not cls.__is_text(sub):
                    return False
                # Return False if sub-tag is not met name required
                if child_name is not None:
                    if sub.tagName != child_name:
                        return False
                # Mark True if sub-tag is text
                ret = True
        # Return check result
        return ret

    @staticmethod
    def __text_in_tag(tag):
        return '' if tag.firstChild is None else tag.firstChild.data.strip()

    @staticmethod
    def __atts_in_tag(tag):
        atts = ((k.strip(), v.strip()) for k, v in tag.attributes.items())
        return dict(atts)

    def __read_tag(self, tag, tag_type=None, child_name=None):

        # Tag is text
        if self.__is_text(tag):

            # Check type if being required
            if tag_type is TextGroupTag:
                raise ValueError('Tag must be a group of text tags: <{:s}>'.format(tag.tagName))

            # Return value
            return TextTag(
                name=tag.tagName,
                text=self.__text_in_tag(tag),
                atts=self.__atts_in_tag(tag),
                index=self.childs.index(tag)
            )

        # Tag containing group of text tags
        if self.__is_textgroup(tag, child_name):

            # Check type if being required
            if tag_type is TextTag:
                raise ValueError('Tag must be a text tag: <{:s}>'.format(tag.tagName))

            # Read sub-tags in tag
            subs = [
                TextTag(
                    name=sub.tagName,
                    text=self.__text_in_tag(sub),
                    atts=self.__atts_in_tag(sub),
                    index=tag.childNodes.index(sub)
                )
                for sub in tag.childNodes if isinstance(sub, Element)
            ]

            # Return tag including its sub-tags
            return TextGroupTag(
                name=tag.tagName,
                tags=subs,
                atts=self.__atts_in_tag(tag),
                index=self.childs.index(tag)
            )

        # For unknown tags
        raise NotImplementedError('Unsupported tag: <{:s}>'.format(tag.tagName))

    def get_tag(self, tagname, tag_type=None, child_name=None):
        """
        Get content of a single tag, that single tag could be text tag or a
        group of text tags

        :param tagname:     Name of tag to get
        :param tag_type:    Require returned tag must be a specific type
        :param child_name:  Name of sub-tag must be met if tag is a group
        :return:            (TextTag | TextGroupTag | None)
        """

        try:
            tag = self.dom.getElementsByTagName(tagname)[0]
            return self.__read_tag(tag, tag_type=tag_type, child_name=child_name)  # tag found
        except IndexError:
            return None  # tag not found

    def get_tags(self, tagname, tag_type=None, child_name=None):
        """
        Get contents of all tags with same tagname being specified

        :param tagname:     Name of tags would like to get
        :param tag_type:    Require returned tag must be a specific type
        :param child_name:  Name of sub-tag must be met if tag is a group
        :return:            (list of TextTag | TextGroupTag, or empty list)
        """

        tags = self.dom.getElementsByTagName(tagname)
        return [self.__read_tag(tag, tag_type=tag_type, child_name=child_name) for tag in tags]


class ReadmeXMLReader(XMLReader):

    def __init__(self, fpath):
        super(ReadmeXMLReader, self).__init__(fpath)

    @property
    def logo(self):
        return self.get_tag('logo', tag_type=TextTag)

    @property
    def title(self):
        return self.get_tag('title', tag_type=TextTag)

    @property
    def author(self):
        return self.get_tag('author', tag_type=TextTag)

    @property
    def license(self):
        return self.get_tag('license', tag_type=TextTag)

    @property
    def files(self):
        return self.get_tag('files', tag_type=TextGroupTag, child_name='file')

    @property
    def paragraphs(self):
        return self.get_tags('paragraph', tag_type=TextTag)
