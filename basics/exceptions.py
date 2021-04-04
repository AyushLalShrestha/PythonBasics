

class MyError(Exception):
    def __init__(self, message, *args):
        self.message = message
        super(MyError, self).__init__(message, *args)

def some_method():
    try:
        execute_method()
    except KeyError as ke:
        print(ke)
    except MyError as ve:
        print(ve)

    
def execute_method():
    raise MyError("My Error, Hehehe")
    print("After the error has been raised")

def main():
    some_method()

if __name__=='__main__':
    main()
