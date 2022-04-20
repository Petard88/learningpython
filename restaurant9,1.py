class Restaurant:
    """A class to model a restaurant list"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialized restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

restaurant_1 = Restaurant('Svarta Pannan', 'Husmanskost')
restaurant_2 = Restaurant('Åsbro Pizzeria', 'Skabbpizza')
restaurant_3 = Restaurant('CoCo Thai', 'Thai food')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
print(f"\n{restaurant_3.restaurant_name}")
print(f"{restaurant_3.cuisine_type}")
