#!/usr/bin/env python3

class Obj_Storage():
    def __init__(self):
        self.obj = {}

    def new(self, obj):
        self.obj[obj.id] = obj

    def all(self):
        return(self.obj)
