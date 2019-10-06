a, b = map(str, input().split(" "))

ab = int(a, 2)
bb = int(b, 2)

print(bin(ab*bb).replace("0b", ""))
