def computeGCD(x, y):
    while y:
        x, y = y, x % y

    return x


a = list(map(int, input().split(" ")))


print((computeGCD(a[0], a[1]) == 1 and "YES") or "NO")
