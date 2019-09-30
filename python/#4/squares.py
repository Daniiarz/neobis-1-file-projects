n_l = list(map(int, input().split(" ")))

for i in range(n_l[0], n_l[1] + 1):
    print("{}*{}={}".format(i, i, i**2))
