prompt = "Enter something: "
prompt += "\nexit"
age = 0
#while age < 5:
#    age += 1
#    print(age)
active = True
while active == True:
    message = input(prompt)

    if message == 'exit':
        active = False
    else:
        print("hej")