#!/usr/bin/env python3
import os.path
from models.documentation_model import Doc
from models.engine.obj_storage import Obj_Storage
from models import file_store

class File():
    count = 0
    
    def __init__(self, file_name):
        self.functions_count = 0;
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
                    new_doc = eval("Doc")(self.functions_count)
                    flag = 1
                if flag is 1:
                    File.check_line(new_doc, line)
                if '*/' in line:
                    self.doc_store.new(new_doc)
                    self.functions_count += 1
                    full_doc = ""
                    flag = 0
    
    @staticmethod
    def check_line(obj, line):
        line = line.strip("* ")
        line = line.strip("\n")
        if "-" in line:
            obj.name = line.split("-")[0]
            obj.description = (line.split("-")[1]).strip()
        if "@" in line:
            obj.arguments.append(line)
        if "Return" in line:
            obj.return_value = line

    @staticmethod
    def write_obj(obj, fd):
        fd.write("# " + obj.file_name + "\n")
        for key, value in obj.doc_store.obj.items():
            File.write_function(value, fd)
        pass

    @staticmethod
    def write_function(func, fd):
        fd.write("## " + func.name + "\n")
        fd.write(func.description + "\n")
        for element in func.arguments:
            fd.write(element + "\n")
        fd.write(func.return_value + "\n")

    @staticmethod
    def write_arguments(arguments):
        pass
