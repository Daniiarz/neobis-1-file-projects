a = int(input())

div = []

for i in range(1, a):
    if i == a//2:
        div.append(i)
        break

    if a % i == 0:
        div.append(i)

if sum(div) == a:
    print("YES")
else:
    print("NO")