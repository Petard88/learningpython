ordinal_numbers = list(range(1, 10))

for number in ordinal_numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number >=4:
        print(f"{number}th")