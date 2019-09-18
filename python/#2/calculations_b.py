import re
import math
import sys

a = sys.stdin.readlines()
# n_l = list(map(float, re.findall("\w.\w+ | \w+", a)))
#
# # print("{}".format(
# #     math.sqrt(
# #         pow((n_l[2] - n_l[0]), 2) + pow((n_l[3] - n_l[1]), 2)
# #     )))
[print(i[:-2]) for i in a]
