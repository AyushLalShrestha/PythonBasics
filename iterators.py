def iterable_func():
    for i in range(10, 25):
        yield i

for j in iterable_func():
    print(j)