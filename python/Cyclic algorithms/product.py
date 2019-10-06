n_l = list(map(int, input().split(" ")))
if n_l[0] < 0:
    print("({})*{}={}".format(n_l[0], n_l[1], n_l[0] * n_l[1]))
elif n_l[1] < 0:
    print("{}*({})={}".format(n_l[0], n_l[1], n_l[0] * n_l[1]))
else:
    print("{}*{}={}".format(n_l[0], n_l[1], n_l[0] * n_l[1]))