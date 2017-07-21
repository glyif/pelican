# /usr/bin/env python3

from collections import namedtuple
from xml.dom.minidom import Element, Text, parse
from xml.parsers.expat import ExpatError

__all__ = [
    'XMLReader',
    'ReadmeXMLReader',
    'TextTag',
    'TextGroupTag'
]

TextTag = namedtuple('TextTag', 'name text atts index')
TextGroupTag = namedtuple('TextGroupTag', 'name tags atts index')


class XMLReader:
    """
    Object that parses the xml file and gives instructions for the MDGen
    """

    def __init__(self, fpath):
        """
        Initialize XMLReader Object

        :param fpath: file path of xml file
        """

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
        """
        checks if there is text inside a tag

        :param tag: xml tag
        :return: 0 if no text, 1 if there is text
        """
        return any([
            len(tag.childNodes) == 0 and tag.firstChild is None,
            len(tag.childNodes) == 1 and isinstance(tag.firstChild, Text)
        ])

    @classmethod
    def __is_textgroup(cls, tag, child_name=None):
        """
        checks if there is a text group inside of a tag
        :param tag: xml tag
        :param child_name: name of child
        :return: True or False
        """

        # init check result
        ret = False
        # load sub-tags
        subs = tag.childNodes
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
        """
        grabs text in tab
        :param tag: xml tag
        :return: returns data in xml tag
        """
        return '' if tag.firstChild is None else tag.firstChild.data.strip()

    @staticmethod
    def __atts_in_tag(tag):
        """
        grabs for attributes in a tag

        :param tag: xml tag
        :return: returns a dictionary of atrributes in the xml tag
        """
        atts = ((k.strip(), v.strip()) for k, v in tag.attributes.items())
        return dict(atts)

    def __read_tag(self, tag, tag_type=None, child_name=None):
        """
        grabs all data from an xml tag

        :param tag: xml tag to grab data from
        :param tag_type: type of xml tag
        :param child_name: name of child
        :return: new TextTag or TextGroupTag tuple
        """

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
    """
    Pelican README gen class - inherits from XMLReader class
    """

    def __init__(self, fpath):
        """
        Initializes ReadmeXMLReader object

        :param fpath: path to xml
        """

        # uses the XMLReader __jnit__ passing in the fpath
        super(ReadmeXMLReader, self).__init__(fpath)

    @property
    def logo(self):
        """
        gets logo tag

        :return: logo tag
        """

        return self.get_tag('logo', tag_type=TextTag)

    @property
    def title(self):
        """
        gets title tag

        :return: title tag
        """

        return self.get_tag('title', tag_type=TextTag)

    @property
    def author(self):
        """
        gets author tag

        :return: author tag
        """

        return self.get_tag('author', tag_type=TextTag)

    @property
    def license(self):
        """
        gets license tag

        :return: license tag
        """

        return self.get_tag('license', tag_type=TextTag)

    @property
    def files(self):
        """
        gets file tag

        :return: file tag
        """

        return self.get_tag('files', tag_type=TextGroupTag, child_name='file')

    @property
    def paragraphs(self):
        """
        gets paragraph tag

        :return: paragraph tag
        """

        return self.get_tags('paragraph', tag_type=TextTag)
