class PartOfUniverse(object):
    def __init__(self, universe_name):
        print("This is the %s %s init method" % ("PartOfUniverse", "Super Class"))
        self.universe_name = universe_name

    def _name_of_universe(self):
        print("The animal is part of the Universe: " + str(self.universe_name))


class Animal(object):
    def __init__(self, name, fav_food, type):
        print("This is the %s %s init method" % ("Animal", "Super Class"))
        self.name = name
        self.fav_food = fav_food
        self.type = type

    def walk(self):
        print("Animal is walking")

    def speak(self):
        print("Animal is speaking")


class Dog(Animal, PartOfUniverse):
    def __init__(self, name, fav_food, breed, universe_name):
        # Precedence to Animal's init since infront
        # super().__init__(name, fav_food, "Dog")
        super(Dog, self).__init__(name, fav_food, "Dog")

        # This won't work
        # super(Dog, self).__init__(universe_name) 

        # Do this instead
        PartOfUniverse.__init__(self, universe_name)

        self.breed = breed

    def __speak(self):
        print("This Dog Barks, BHOU-BHOU")

    def getNameBreed(self):
        self.__speak()
        print(self.name + " is of " + self.breed + " Breed")


def main():
    snoie = Dog("Snoie", "Mo:Mo", "JapaneseSpitz", "MilkyWay")

    # print(dir(snoie)) 
    # print(snoie.__dict__)

    snoie._Dog__speak()

    func_get = getattr(snoie, "speak")
    func_get()

    snoie._name_of_universe()
    print(snoie.__class__)
    print(type(snoie))


if __name__ == '__main__':
    main()
