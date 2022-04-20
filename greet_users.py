def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:# För varje grej i listan gör det här
        msg = f"Hello, {name.title()}!"# sätt msg som det formaterade meddelandet
        print(msg)# (f"Hello, {name.title()}!") samma funktion

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames) # skickar listan usernames till funktionen greet_users