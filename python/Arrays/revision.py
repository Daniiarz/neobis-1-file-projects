a = input()

print(str(sorted(list(map(int, input().split(" "))))[:2])[1:-1].replace(",", ""))
