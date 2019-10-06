a = int(input())

result = ""

for i in range(1, a+1):
    is_cool_digit = True

    for k in str(i):
        k = int(k)

        if k != 0 and i % k != 0 or k == 0:
            is_cool_digit = False

    if is_cool_digit:
        result += "{} ".format(i)


print(result.strip())
