import sys

from builtins import print


class Animal():
    def walk(self):
        print("Animal is walking")

    def speak(self):
        print("Animal is speakind")

class Dog(Animal):
    def speak(self):
        print("This Animal Barks, BHOU-BHOU")

    def __init__(self, dogName, dogBreed):
        self.__breed = dogBreed
        self.__name = dogName

    def getNameBreed(self):
        print(self.__name +" is of " + self.__breed + " Breed")

def main():
    snoie = Dog("snowie", "JapaneseSpitz")
    snoie.speak()
    snoie.walk()
    snoie.getNameBreed()



if __name__ == '__main__':
    main()

