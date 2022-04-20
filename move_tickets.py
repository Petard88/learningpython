prompt = "Enter your age: "
prompt += "\nEnter 'quit' to exit program."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("The price of your ticket is $0")
    elif int(age) < 12:
        print("The price of your ticket is $10")
    elif int(age) >= 12:
        print("The price of your ticket is $15")