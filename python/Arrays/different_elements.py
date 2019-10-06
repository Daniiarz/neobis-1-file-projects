a = input()

score_list = sorted(list(map(int, input().split(" "))))

result = []

for i in score_list[::-1]:
    if i not in result:
        result.append(i)

print(len(result))
