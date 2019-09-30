def n_m():
    num = int(input())
    return (
            (num in range(1, 3) and "Winter")
            or (num in range(3, 6) and "Spring")
            or (num in range(6, 8) and "Summer")
            or (num in range(9, 12) and "Autumn")
            or (num == 12 and "Winter")
            or "Wrong number"
            )


print(n_m())
