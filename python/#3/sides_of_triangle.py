def sides():
    s_l = sorted(list(map(int, input().split(" "))))
    return (
            (s_l[2] > s_l[2] + s_l[1] and s_l[0] < s_l[2] - s_l[1] and "YES")
            or (sum(s_l) / 3 == s_l[1] and "YES")
            or "NO"
    )


print(sides())
