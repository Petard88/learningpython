filename = 'programming_poll_list.txt'
prompt = '\nWhy do you like programming? (Type quit to exit)\n'

while True:
    with open(filename, 'a') as file_object:
        reason = input(prompt)
        if reason.lower() == 'quit':
            break
        else:
            file_object.write(f'{reason}\n')