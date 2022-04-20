number = input("Tell me a number and I will tell you if it is a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print("it is")
else:
    print("nope")