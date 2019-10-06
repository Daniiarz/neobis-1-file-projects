a = list(map(int, list(input())))

if len(a) % 2 != 0:
    print(sum(a))
else:
    print(sum(a[:(len(a)//2)]))
