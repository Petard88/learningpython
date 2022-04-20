sandwiches = ['tuna', 'pastrami', 'blt', 'teriyaki', 'pastrami', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwiches:
    print(f"We are out of pastrami!")
    sandwiches.remove('pastrami')
while sandwiches:
    current_sandwich = sandwiches.pop()

    print(f"Making your {current_sandwich.title()}!")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"--{sandwich.title()}--")