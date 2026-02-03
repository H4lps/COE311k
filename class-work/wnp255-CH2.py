import math

def int_to_bin(n : int):
    s = ""
    while (n > 0):
        if (n % 2):
            s = "1" + s
        else:
            s = "0" + s
        n = math.floor(n/2)
    return s

print(int_to_bin(2025))
assert(int_to_bin(5) == "101")
assert(int_to_bin(16) == "10000")
