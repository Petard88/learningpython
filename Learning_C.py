filename = 'learning_python.txt'

content = ''
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    content += line.replace('python','c')

print(content)

