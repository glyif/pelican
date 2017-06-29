#!/usr/bin/env python3
import os.path
from models import obj_store

class Documentation():
    count = 0
    
    def __init__(self, file_name):
        self.id = Documentation.count
        Documentation.count += 1
        self.file_name  = file_name
        self.file_type = os.path.splitext(self.file_name)[1]
        obj_store.new(self)
