def make_pizza(*toppings):
    #"""Print the list of toppings that have been requested"""
    #print(toppings)
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following ingredients:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni', 'smör', 'kalvdans')
