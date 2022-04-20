# Dictionaries in dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }

    }
# loops through the users dictionary. assigns each key to the variable username and their respective dictionary to
# the variable user_info
for username, user_info in users.items():
    print(f"\nUsername: {username}") # prints the username
    full_name = f"{user_info['first']} {user_info['last']}" # sets the variable full name to be the values in they specified keys
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")