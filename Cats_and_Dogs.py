filenames = ['cats.txt', 'dogs.txt', 'hej.txt']

try:
    for filename in filenames:
        with open(filename) as f:
            content = f.read()
            print(content)
except FileNotFoundError:
    pass
