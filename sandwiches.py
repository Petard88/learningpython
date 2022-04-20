def ordered_sandwich(*toppings):
    print(f"Making a sandwich with:")
    for topping in toppings:
        print(f"\t*{topping.title()}")


ordered_sandwich('ost', 'smör', 'gurka', 'korv', 'tomat')
ordered_sandwich('smör', 'ost')
ordered_sandwich('bröd', 'smör')