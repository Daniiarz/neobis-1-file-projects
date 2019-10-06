a = input()
b = list(map(int, input().split(" ")))
c = int(input())

d = 1

result = []

while c in b:
    i = b.index(c)
    result.append(str(i + d))
    b.pop(i)
    d += 1

print(" ".join(result))
