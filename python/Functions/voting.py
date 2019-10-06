num = int(input())

result = []


def voting_result(kek):
    c0 = 0
    c1 = 0
    for k in kek:
        if k == "1":
            c1 += 1
        else:
            c0 += 1

    return (c0 > c1 and "0") or "1"


for i in range(num):
    result.append(voting_result(input().split(" ")))

print("\n".join(result))
