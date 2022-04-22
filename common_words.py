filenames = ['alice.txt', 'moby_dick.txt']

try:
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            dick_counter = content.lower().count('dick')
            print(dick_counter)
except FileNotFoundError:
    pass
