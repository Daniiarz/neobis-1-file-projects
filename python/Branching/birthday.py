import datetime

date = list(map(int, input().split(" ")))

print(datetime.datetime(2016, date[1], date[0]).strftime("%A"))
