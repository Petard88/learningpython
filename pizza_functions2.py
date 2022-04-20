def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following ingredients:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(200, 'mushrooms', 'ost', 'korv')
make_pizza(12, 'ost')