favorite_numbers = {
    'Kurt': [1, 2],
    'Bengt': [3, 4],
    'Åke': [5, 6],
    'Nils-Karlsson Pyssling': [7, 8],
    'Bo': [9, 10],
    }
print(f"Favorite numbers:\n{favorite_numbers}")

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t {number}")