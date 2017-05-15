def barking(cls):
    for methode in dir(cls): # cls.__dict__
        if methode.startswith("__"):
            continue
        func = getattr(cls, methode) # cls.__dict__[name]
        def woofer(*args, **kwargs):
            print("Woof Woof !!")
            return func(*args, **kwargs)
        setattr(cls, methode, woofer) # redefines 'methode' method of cls as Woofer
    return cls

@barking
class Animal():
    def __init__(self, name):
        self.__name = name
    def shout(self):
        print(self.__name + "This Animal is Shouting")
    def walk(self):
        print(self.__name + " Animal is Walking !!")


doggy = Animal("Snoie");
print(dir(doggy));
doggy.walk();
doggy.shout();
