import re
import math


n_l = list(map(int, re.findall("\w.\w+ | \w+", input())))

print("{}".format(
    math.sqrt(
         pow((n_l[2] - n_l[0]), 2) + pow((n_l[3] - n_l[1]), 2)
     )))

