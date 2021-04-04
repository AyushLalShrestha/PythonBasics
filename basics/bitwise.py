#!/usr/local/bin/python3

a = 0b00000001
is_a_even = (a ^ 1 == a + 1)
print(f"{int(a)} => Bits:{a.bit_length()}, is_even:{is_a_even}")

print( bin(240), bin(0b11110000))

# 1's complement
print(~0b11110000, bin(~0b11110000))

# -ve representation
print(bin(58), bin(-58))

def get_twos_complement(a):
    if a < 0:
        return a + (1 << a.bit_length())
    return a

"""
In python, the not of 240 is shown as -241, this is because:
    240 => 2's complement => 011110000
    011110000 => not => 100001111
    Which is 2's complement representation of -241
"""

