#!/usr/bin/env python3

from models import obj_store
from models.base_model import Documentation

d1 = Documentation("hello.py")
d2 = Documentation("hello.c")
d3 = Documentation("hello.js")

print("{} {} {}".format(d1.file_type, d2.file_type, d3.file_type))
