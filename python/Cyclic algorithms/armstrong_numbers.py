def is_armstrong(number):
    return sum([int(k) ** len(str(number)) for k in str(number)]) == number


for i in range(100, 1000):
    if is_armstrong(i):
        print(i)

