a = list(map(int, list(input())))[::-1]

result = ""

for i in a:
    result += "{}+".format(i)

print(result[:-1]+"={}".format(sum(a)))
