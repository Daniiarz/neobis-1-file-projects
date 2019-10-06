import math

num = int(input())
hours = math.floor(num / 3600)
minutes = math.floor(num / 60) - (hours * 60)
seconds = num - (hours*3600 + minutes*60)

print("{} {} {}".format(hours, minutes, seconds))
