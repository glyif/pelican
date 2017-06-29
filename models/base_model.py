#!/usr/bin/env python3
from models import obj_store

class Documentation():
    count = 0
    
    def __init__(self):
        self.id = Documentation.count
        Documentation.count += 1
        obj_store.new(self)
