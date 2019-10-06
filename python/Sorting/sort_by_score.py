def listify(k):
    return list(map(int, input().split(" ")))


a = input()

result = []

for i in range(int(a)):
    result.append(listify(input()))

