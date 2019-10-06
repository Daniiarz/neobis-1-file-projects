a = input()
b = list(map(int, input().split(" ")))
c = int(input())

result = []


def kek():
    for i in b:
        result.append(abs(i - c))

    if c in b:
        return c

    elif min(b) > c:
        return c + sorted(result)[0]

    else:
        return c - sorted(result)[0]


print(kek())
