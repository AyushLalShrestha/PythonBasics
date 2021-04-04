import sys

a = 0xcafebabe
print(f"Big a = {int(a).to_bytes(length=4, byteorder='big')}")
print(f"Sys a = {int(a).to_bytes(length=4, byteorder=sys.byteorder)}")


"""
In python, the not of 240 is shown as -241, this is because:
    240 => 2's complement => 011110000
    011110000 => not => 100001111
    Which is 2's complement representation of -241
"""
a = 0b11110000  # 240
a_comp = bin(~a)  # -241 == 100001111
a_comp_bytes = int(~a).to_bytes(2, byteorder=sys.byteorder, signed=True)
print(bin(a_comp_bytes[0]))  # last part of 2's comp representation of -241



