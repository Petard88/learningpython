filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(input("What is your name? \n"))