a = input()
b = list(map(int, input().split(" ")))
c = len(b)

part1 = sorted(b[:c//2])
part2 = sorted(b[c//2:])[::-1]

print(str(part1)[1:-1].replace(",", ""), str(part2)[1:-1].replace(",", ""))

