filenames = ['alice.txt', 'moby_dick.txt', 'halo.txt', 'siddhartha.txt', 'little_women.txt']
the_word = input("What word are you looking for? ")
try:
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            word_counter = content.lower().count(the_word.lower())
            print(f"The word '{the_word.title()}' occurs {word_counter} times in '{filename}'.")
except FileNotFoundError:
    pass
