age = 56

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: # avsluta med ett elif istället för ett else för att göra koden tydligare
    price = 20  # och bara acceptera input i rätt "format"

print(f"Your price is {price} dollarydoos.")
