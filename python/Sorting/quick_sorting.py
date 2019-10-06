def stringify(k):
    return str(k)[1:-1].replace(",", "")


a = input()
b = sorted(list(map(int, input().split(" "))))


result = []

for i in b:
    if i not in result:
        result.append(i)

print(len(result))
print(stringify(b))
