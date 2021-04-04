"""
Else clauses in while/for loops are "No Break" clauses, i.e
they will only execute if "break" was not hit in the loop.
"""

def iterable_func():
    for i in range(10, 15):
        yield i

# iterables
for i in iterable_func():
    if i > 12:
        break
    print(i)
else:
    print("Else block; Since for complete")

# for-else
for j in range(20, 25):
    print(j)
else:
    print("Else block; Since for loop complete")

# while-else
count = 5
while count > 0:
    print(count)
    count -= 1
    if count == 2:
        break
else:
    print("Else block; Since while loop did not 'break' ")
