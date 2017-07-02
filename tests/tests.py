#!/usr/bin/env python3
from models import file_store
from models.file_model import File
from models.documentation_model import Doc

global fd
fd = open("test.md", "w+")

test = File("file.c")

test.write_obj(test, fd)
