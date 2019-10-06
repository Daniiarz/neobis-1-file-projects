num_list = list(map(int, input().split(" ")))


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def kek(a):
    kek_list = []
    for i in range(a[0], a[1]):
        if is_prime(i):
            kek_list.append(i)

    return kek_list


print(str(kek(num_list))[1:-1].translate({",": ""}))
