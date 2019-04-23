import sys
from abc import abstractmethod

# from builtins import print

class PartOfUniverse(object):
    def __init__(self, universe_name):
        print("This is the %s %s init method" %("PartOfUniverse" , "Super Class") )
        self.universe_name = universe_name
    
    def _name_of_universe(self):
        print("The animal is part of the Universe: " + str(self.universe_name) )

class Animal(object):
    def __init__(self, name, fav_food, type):
        print("This is the %s %s init method" %("Animal", "Super Class") )
        self.name = name
        self.fav_food = fav_food
        self.type = type

    def walk(self):
        print("Animal is walking")

    def speak(self):
        print("Animal is speaking")

class Dog(Animal, PartOfUniverse):
    def __init__(self, name, fav_food, breed, universe_name):
        super(Dog, self).__init__(name, fav_food, "Dog")
        # PartOfUniverse.__init__(self, universe_name)
        super(Dog, self).__init__(name, universe_name)
        #super(Dog, self).__init__(universe_name)
        # Animal.__init__(self, name, fav_food, "Dog")
        # super().__init__(name, fav_food, "Dog")
        self.breed = breed

    def __speak(self):
        print("This Animal Barks, BHOU-BHOU")

    def getNameBreed(self):
        self.__speak()
        print(self.name +" is of " + self.breed + " Breed")

def main():
    snoie = Dog("snowie", "FihsChips", "JapaneseSpitz", "MilkyWay")
    snoie._Dog__speak()
    snoie._name_of_universe()
    #snoie.speak()
    #snoie.walk()
    #snoie.getNameBreed()
    print("This is the DIR: ")
    print(dir(snoie))
    '''
    print("This is the DICT: ")
    print(snoie.__dict__)
    '''
    func_get = getattr(snoie, "speak")
    func_get()

if __name__ == '__main__':
    main()


