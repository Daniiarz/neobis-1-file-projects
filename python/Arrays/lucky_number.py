def lucky():
    a = int(input())

    if len(str(a)) != 4 or a % 2 != 0:
        return "unlucky"

    a = list(map(int, str(a)))

    return (sum(a[:len(a)//2]) == sum(a[len(a)//2:]) and "lucky") or "unlucky"


print(lucky())
