# How a function can also be passed around as a variable and an object

def funct(x):
    def decFunct(n):
        return(x * n)
    return decFunct

receptor = funct(10)  # x = 10
answer = receptor(3)  # n = 3
print(answer)


def hello_function():
            print( "This is a Hello Function" )

def deco_function(func):
            func()

deco_function(hello_function)






