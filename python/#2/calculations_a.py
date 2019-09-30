import re

a = input()
n_l = list(map(int, re.findall("\w", a)))

print("{}+{}+{}={}".format(n_l[0], n_l[1], n_l[2], sum(n_l)))
print("{}*{}*{}={}".format(n_l[0], n_l[1], n_l[2], n_l[0]*n_l[1]*n_l[2]))
print("({}+{}+{})/{}={}".format(n_l[0], n_l[1], n_l[2], len(n_l), round(sum(n_l) / len(n_l), 3)))
