age_list = list(map(int, input().split(" ")))


def oldest(anton, boris, victor):
    if anton == boris == victor:
        return "Same age"

    elif anton == max(age_list):
        return (anton == boris and "Victor") or (anton == victor and "Boris") or "Anton"

    elif boris == max(age_list):
        return (boris == anton and "Victor") or (boris == victor and "Anton") or "Boris"

    else:
        return (victor == anton and "Boris") or (boris == victor and "Anton") or "Victor"


print(oldest(age_list[0], age_list[1], age_list[2]))
