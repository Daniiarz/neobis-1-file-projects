a = int(input())


def is_leap_year(year):
    return (year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0) and "YES" )or "NO"


print(is_leap_year(a))
