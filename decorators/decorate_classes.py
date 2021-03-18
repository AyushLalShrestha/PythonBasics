

def decorator(func,):
    def wrapper(obj=None):
        if getattr(obj, 'name'):
            obj.name = 'Changed Name'
        print("Wrapper start")
        res = func(obj)
        print(res)
        print("Wrapper end")
    return wrapper


class Person(object):
    def __init__(self,):
        self.name = "Ayush"

    @decorator
    def f1(self,):
        print(f"f1: name={self.name}")
    
    def f2(self,):
        self.name = "Shrestha"
        print(f"f2: name={self.name}")

p1 = Person()
p1.f1()