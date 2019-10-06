num_list = list(map(int, list(input())))


def find(a):

    for i in range(len(a)):
        if i == len(a) - 1:
            return "NO"

        if a[i] == a[i + 1]:
            return "YES"

    return "NO"


print(find(num_list))
