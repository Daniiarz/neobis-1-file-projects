import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


sides = list(map(float, input().split(" ")))
perimeter = 0


def area_func(s_l):
    return 0.5 * abs((s_l[2] - s_l[0]) * (s_l[5] - s_l[1]) - (s_l[4] - s_l[0]) * (s_l[3] - s_l[1]))


area = area_func(sides)

d = -2
while d < 4:
    perimeter += distance(sides[d], sides[d+1], sides[d+2], sides[d+3])
    d += 2

print(round(perimeter, 5), round(area, 2))
