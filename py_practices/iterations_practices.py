#!/usr/bin/bash python
# source: https://youtu.be/OSGv2VnC0go
colors = ['red', 'blue', 'yellow']
color_codes = ['r', 'b', 'y']
numbers = [1, 2, 3, 4, 5]

#1. xrange instead of range
for i in xrange(1, 10, 2 ):
    print(i)

#2. use reversed to iterate in reverse
for i in reversed(colors):
    print(i)

#3. use enumerate to iterate over collection with indices
for i, color in enumerate(colors):
    print(color)

#4. joining 2 lists
for code, color in izip(color_codes, colors):
    print(code, color)

#5. call a function using a sentinel value
f = open('/tmp/some.txt', 'r')
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

#6. use for-else
'''
for i in numbers:
    if i > 5:
        break
else:
    return "No number greater than 5"
return "A number was greater than 5"
'''

#7. 