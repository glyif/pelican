#!/usr/bin/env python3

import xml.etree.cElementTree as ET
import os

def title_gen(attrib, fd):
    cwd = os.getcwd()
    cwd = os.path.basename(cwd)
    fd.write("# " + cwd + '\n')

def image_gen(attrib, fd):
    fd.write("<img src=" + "\"" + attrib.get("src") + "\">" + '\n')

def parseXML(xml_file, fd):
    """
    Parse XML with ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()

    fp = {
        "title" : title_gen,
        "image" : image_gen
    }

 
    readme = root.getchildren()
    for element in readme:
        fp[element.tag](element.attrib, fd)

     
if __name__ == "__main__":
    with open("README.md", "w+") as fd:
        parseXML("readme.xml", fd)
