a = int(input())

print(str(list(map(int, input().split(" ")))[::-1])[1:-1].replace(",", ""))
