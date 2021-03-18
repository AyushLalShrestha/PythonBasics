
def decorator_factory(regen):
    def decorator(func):
        def wrapper(obj=None):
            if getattr(obj, 'name'):
                obj.name += '__'
            res = func(obj)
            print(res)
            if regen == 'tabs':
                print('regenerating tabs')
            else:
                print('regenerating widgets')
        return wrapper
    return decorator

class Person(object):
    def __init__(self,):
        self.name = "Ayush"

    @decorator_factory('widget')
    def f1(self,):
        return f"f1: name={self.name}"
    
    def f2(self,):
        self.name = "Shrestha"
        print(f"f2: name={self.name}")

p1 = Person()
p1.f1()