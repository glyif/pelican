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
                    new_doc = eval("Doc")(full_doc)
                    flag = 1
                if flag is 1:
                    File.check_line(new_doc, line)
                    full_doc = full_doc + line
                if '*/' in line:
                    self.doc_store.new(new_doc)
                    full_doc = ""
                    flag = 0
    
    @staticmethod
    def check_line(obj, line):
        line = line.strip("* ")
        if "-" in line:
            obj.name = line.split("-")[0]
            obj.description = (line.split("-")[1]).strip()
            print("{} \n{}".format(obj.name, obj.description))
        if "@" in line:
            obj.arguments.append(line)
        if "Return" in line:
            obj.return_value = line
            print(obj.return_value)
        print(obj.arguments)
