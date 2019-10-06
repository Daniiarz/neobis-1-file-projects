a = int(input())

result = []

for i in range(a):
    result.append(int(input()))

print("\n".join(map(str, sorted(result))))
