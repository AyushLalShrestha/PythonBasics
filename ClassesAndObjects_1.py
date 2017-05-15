import sys

from builtins import print


class Animal():
    def __init__(self, name, fav_food, type):
        self.name = name
        self.fav_food = fav_food
        self.type = type

    def walk(self):
        print("Animal is walking")

    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def __init__(self, name, fav_food, breed):
        super(Dog, self).__init__(name, fav_food, "Dog")
        # Animal.__init__(self, name, fav_food, "Dog")
        #super().__init__(name, fav_food, "Dog")
        self.breed = breed

    def speak(self):
        print("This Animal Barks, BHOU-BHOU")

    def getNameBreed(self):
        print(self.name +" is of " + self.breed + " Breed")

def main():
    snoie = Dog("snowie", "FihsChips", "JapaneseSpitz")
    snoie.speak()
    snoie.walk()
    snoie.getNameBreed()



if __name__ == '__main__':
    main()

