# Main use of the decorator = wrapping a function

def decorator_func(func):
    def dec_func_in():
        print("---- This is the Start of The Main Decorator !!")
        func()
        print("---- This is the Start of The Main Decorator !!")
    return dec_func_in

# @decorator_func

def function_needs_decorator():
    print("This function needs a Decorator ! ")


function_needs_decorator = decorator_func(function_needs_decorator)
function_needs_decorator()