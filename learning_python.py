filename = 'learning_python.txt'

stuff_list = ''
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.upper())
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    stuff_list += line


print(stuff_list.title())
