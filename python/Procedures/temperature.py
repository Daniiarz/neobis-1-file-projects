from ctypes import *
aa = int(input())


def find_temp(a):
    return int((a * 1.8) + 32)


bb = c_int().value = find_temp(aa)

print(bb)
