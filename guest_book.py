filename = 'guest_book.txt'
prompt1 = '\nType quit to exit program.\n'
prompt2 = 'Hello! What is your name? \n'
full_prompt = prompt1 + prompt2

while True:
    with open(filename, 'a') as file_object:
        guest_name = input(full_prompt)
        if guest_name == 'quit':
            break
        else:
            file_object.write(str(f'{guest_name.title()}\n'))
            print(f'Hello, {guest_name.title()}!')
