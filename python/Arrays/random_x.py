from random import randrange

a, b = map(int, input().split(" "))

x_list = []

result = []

for i in range(a):
    c = randrange(6)

    x_list.append(c)

    if c == b:
        result.append(i)


print(" ".join(map(str, x_list)))
print("\n".join(map(str, result)))
