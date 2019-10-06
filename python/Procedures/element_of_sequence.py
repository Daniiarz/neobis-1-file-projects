a = int(input())

s_l = [1, 2, 3]

for i in range(a-3):
    le = len(s_l)
    num = s_l[le - 1] + s_l[le - 2] - 2 * s_l[le - 3]
    s_l.append(num)

print(s_l[len(s_l)-1])
