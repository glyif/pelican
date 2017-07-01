#!/usr/bin/env python3

from models import file_store
from models.file_model import File
from models.documentation_model import Doc

test = File("file.c")
print(test.doc_store.all())
