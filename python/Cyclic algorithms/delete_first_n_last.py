a = input()[1:-1]

for i in a:
    if i == "0":
        a = a[1:]
    else:
        break
print(a)
