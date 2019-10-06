a = list(map(int, list(input())))
result = 0
d = 0

while d < len(a):
    result += a[d]
    d += 2

print(result)
