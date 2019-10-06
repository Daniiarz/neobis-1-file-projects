a = int(input())

result = []


def xor(int1, int2):
    if int1 == "1" and int2 == "1" or int2 == "0" and int1 == "0":
        return "0"
    else:
        return "1"


for i in range(a):
    b1, b2 = map(str, input().split(" "))
    result.append(xor(b1, b2))

print("\n".join(result))
