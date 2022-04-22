import remember_me

username = remember_me.get_stored_username()
print(f"Are you {username}?")
answer= input("Enter y/n: ")

if answer.lower() == 'y':
    remember_me.greet_user()
elif answer.lower() == 'n':
    remember_me.get_new_username()
    username = remember_me.get_stored_username()
    print(f"We'll remember you, {username}!")
else:
    print(f"Please enter 'y' for yes or 'n' for no")
