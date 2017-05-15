import time

def calculates_time(func):
    def calculate_time_taken(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print("The process took : " + str((finish - start) *1000000000000) + " microseconds")
        return result
    return calculate_time_taken        

# @calculates_time
def find_square(series):
    y = 0
    for x in series:
        y += (x * x)
    return y

@calculates_time
def find_cube(series):
    y = 0
    for x in series:
        y += (x * x * x)
    return y

# sqr = find_square(range(3, 1000000))
find_square = calculates_time(find_square)
sqr = find_square(range(3, 1000000))
print(sqr)

cub = find_cube(range(3, 100))
print(cub)


