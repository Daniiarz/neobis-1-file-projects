num_list = list(map(int, list(input())))
odd = 0
even = 0

for i in num_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd, even)
