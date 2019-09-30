import math

points1 = list(map(float, input().split(" ")))
points2 = list(map(float, input().split(" ")))


def area_func(s_l):
    return 0.5 * abs((s_l[2] - s_l[0]) * (s_l[5] - s_l[1]) - (s_l[4] - s_l[0]) * (s_l[3] - s_l[1]))


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pypho(s1):
    return s1[2] ** 2 == s1[0] ** 2 + s1[1] ** 2


def is_rectangle(s1, s2):
    if area_func(s1) != area_func(s2):
        return "NO"

    sides1_ = []
    sides2_ = []

    for i in range(2):
        if i == 1:
            s_list = sides2_
            sides = s2
        else:
            s_list = sides1_
            sides = s1

        d = -2
        while d < 4:
            s_list.append(distance(sides[d], sides[d + 1], sides[d + 2], sides[d + 3]))
            d += 2

        s_list.sort()

    print(sides1_)
    print(sides2_)

    return (sides1_ == sides2_ and pypho(sides1_) == pypho(sides2_) and "YES") or "NO"


print(is_rectangle(points1, points2))
