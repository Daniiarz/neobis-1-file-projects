from random import randrange

a = int(input())

x_list = []

for i in range(a):
    x_list.append(randrange(-100, 101))

print(" ".join(map(str, x_list)))

