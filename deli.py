sandwiches = ['tuna', 'pastrami', 'blt', 'teriyaki']
finished_sandwiches = []

while sandwiches:
    current_sandwich = sandwiches.pop()

    print(f"Making your {current_sandwich.title()}!")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"--{sandwich.title()}--")