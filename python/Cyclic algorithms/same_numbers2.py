num_list = list(map(int, list(input())))


def find(a) -> str:
    b = []

    for i in num_list:
        if i in b:
            return "YES"
        else:
            b.append(i)

    return "NO"


print(find(num_list))
