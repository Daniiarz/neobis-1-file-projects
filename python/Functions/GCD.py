def computeGCD(x, y):
    while y:
        x, y = y, x % y

    return x


a, b = map(int, input().split(" "))


print("GCD({},{})={}".format(a, b, computeGCD(a, b)))
