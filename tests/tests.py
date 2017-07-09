#!/usr/bin/env python3
import glob
from models import file_store
from models.file_model import File
from models.documentation_model import Doc

global fd
fd = open("test.md", "w+")

files_obj = {}
files = glob.glob("/home/vagrant/pelican/*.c")

for item in files:
    files_obj[item] = File(item)

test = File("file.c")

for key, value in files_obj.items():
    File.write_obj(value, fd)
