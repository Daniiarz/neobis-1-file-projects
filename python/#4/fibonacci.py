num_input = int(input())


def fibonacci(num):
    if num <= 0: return "ERROR"

    j = 0
    k = 1
    fibonacci_nums = [0, 1]

    for i in range(num):
        f_num = fibonacci_nums[j] + fibonacci_nums[k]
        if f_num >= num:
            break
        fibonacci_nums.append(f_num)
        j += 1
        k += 1

    return sum(fibonacci_nums)


print(fibonacci(num_input))
