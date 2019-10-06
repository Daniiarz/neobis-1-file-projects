def angles():
    a_l = sorted(list(map(int, input().split(" "))))
    return (
        (0 in a_l and "NO")
        or (sum(a_l) != 180 and "NO")
        or "YES"
    )


print(angles())
