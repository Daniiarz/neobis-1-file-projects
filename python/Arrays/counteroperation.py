marks = list(map(int, input().split(" ")))[1:]

m_min = str(min(marks))
m_max = str(max(marks))

print(str(marks)[1:-1].replace(",", "").replace(m_max, m_min))
