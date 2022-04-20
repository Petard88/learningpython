responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit any place in the world, where would you go? ")

    responses[name] = response #responses[name] blir key och response blir value

    repeat = input("Would you like to let another person take the poll? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Complete ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}.")