def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        return num_words



def txt_word_counter(filenames):
    """Counts how many times a specific word occurs out of all the words from a list of txt files"""
    the_word = input("What word are you looking for? ")
    try:
        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                word_counter = content.lower().count(the_word.lower())
                quotient = int(word_counter) / int(count_words(filename))
                percentage = quotient * 100
                print(
                    f"The word '{the_word.title()}' occurs {word_counter} times in "
                    f"'{filename}' out of {count_words(filename)} words. That is about {round(percentage)}%."
                )


    except FileNotFoundError:
        pass
