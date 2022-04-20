# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'], # List inside a dictionary
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
      f" with the following toppings:")
for topping in pizza['toppings']:# Pulls from the list in the dictionary
    print(f"\t{topping.title()}")