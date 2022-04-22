import json

def get_stored_number():
    """Get favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_number():
    """Prompt favorite number."""
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def tell_number():
    """Prints favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"Your favorite number is {favorite_number}!")
    else:
        favorite_number = get_new_number()
        print(f"We'll remember that your favorite number is {favorite_number}!")

tell_number()
