aa = input()


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_super_prime(a):
    for k in a:
        if is_prime(int(k)):
            pass
        else:
            return "NO"

    return "YES"


print(is_super_prime(aa))

