"""
Object Internals in Python OOP!!

__getattr__ : extracting an attribute of an object
    eg. animal.name
__setattr__ : setting an attribute of an object
    eg. animal.name = "Snoie"
__repr__ : define how a class will be represented
"""

class Vector:

    def __init__(self, **coords):
        self.__dict__.update(**coords)
        self._name="ayush"

    
if __name__ == "__main__":
    v = Vector(x=1, y=2)
    print(dir(v))
    v._name = "ayushq"
    print(vars(v))

