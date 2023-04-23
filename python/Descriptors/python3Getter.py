

import os

# python 3

class Getter:
    def __get__(self, obj, objtype=None): 
        return obj.name

class Founder:
    getter=Getter() # descriptor instance
    def __init__(self):
        self.name="founder"
        # print("founder initialized")

class Manager:
    getter=Getter() # descriptor instance
    def __init__(self):
        self.name="manager"
        # print("manager here")

def python3Getter():
    founder = Founder()
    print(founder.getter)

    manager = Manager()
    print(manager.getter)
python3Getter()