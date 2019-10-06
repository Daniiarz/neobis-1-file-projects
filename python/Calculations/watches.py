n_l = list(map(int, input().split(" ")))
if len(n_l) == 3:
    print(n_l[0]*60*60 + n_l[1]*60 + n_l[2])
if len(n_l) == 2:
    print(n_l[0]*60*60 + n_l[1]*60)
if len(n_l) == 1:
    print(n_l[0]*60*60)
