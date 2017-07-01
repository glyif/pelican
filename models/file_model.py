#!/usr/bin/env python3
import os.path
from models.documentation_model import Doc
from models.engine.obj_storage import Obj_Storage
from models import file_store

class File():
    count = 0
    
    def __init__(self, file_name):
        self.doc_store = Obj_Storage()
        self.id = File.count
        File.count += 1
        self.file_name  = file_name
        self.file_type = os.path.splitext(self.file_name)[1]
        self.parse_file()
        file_store.new(self)

    def parse_file(self):
        full_doc = ""
        flag = 0
        with open(self.file_name) as fd:
            for line in fd:
                if '/**' in line:
                    flag = 1
                if flag is 1:
                    full_doc = full_doc + line
                if '*/' in line:
                    new_doc = eval("Doc")(full_doc)
                    self.doc_store.new(new_doc)
                    full_doc = ""
                    flag = 0
        #create new Doc class per function
        #store Doc class in self.doc_store
        pass
