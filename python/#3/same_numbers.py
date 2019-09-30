num_list = sorted(list(map(int, input().split(" "))))


def same_elements(num1, num2, num3):
    count = 3

    if sum(num_list) / 3 == num1:
        return count
    else:
        return (num1 == num2 and count - 1) or (num2 == num3 and count - 1) or count - 2


print(same_elements(num_list[0], num_list[1], num_list[2]))
