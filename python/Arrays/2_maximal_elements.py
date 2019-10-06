from random import randrange

a = int(input())

x_list = []

for i in range(a):
    x_list.append(randrange(-100, 101))

print(" ".join(map(str, x_list)))

if len(x_list) == 1:
    print("{} {}\n-1".format(x_list[0], 0))

else:
    num1 = max(x_list)
    indx1 = x_list.index(num1)

    x_list[indx1] = min(x_list)

    num2 = max(x_list)
    indx2 = x_list.index(num2)

    print("{} {}\n{} {}".format(num1, indx1, num2, indx2))




