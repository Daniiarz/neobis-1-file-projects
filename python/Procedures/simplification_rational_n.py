import math
from ctypes import *

in1, in2 = map(int, input().split())


def kek(a, b, c):
    c.value = "{}/{}".format(a // math.gcd(a, b), b // math.gcd(a, b))


k = c_wchar_p

kek(in1, in2, k)

print(k)

