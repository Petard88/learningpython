print("Give me numbers, I'll add them together!")
print("Enter 'q' to quit.")
total = []

while True:
    number = input("Give me a number: ")
    if number == 'q':
        break

    try:
        total.append(int(number))
    except ValueError:
        print("Use numbers.")
    else:
        print(sum(total))
        