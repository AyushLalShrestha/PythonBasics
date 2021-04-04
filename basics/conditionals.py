import sys

def ageCalc(age):
    if (20 > age > 10):
        print("You are A big boy now")
    elif (20 < age < 40):
        print("You are in your working life")
    elif (40 < age < 60):
        print("You are getting old :)")
    else:
        print("You are a Child or an Old man :)")

age = eval(input("Enter age: "))
ageCalc(age)


