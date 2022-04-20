class Restaurant:
    """A class to model a restaurant list"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialized restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number):
        """Sets the number of customers served to the specified value."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't decrease the customer count.")

    def increment_number_served(self, customers):
        """Increments the number of customers who have been served at this restaurant."""
        if customers >= 0:
            self.number_served += customers
        else:
            print("You can't decrease the customer count.")


restaurant_1 = Restaurant('Svarta Pannan', 'Husmanskost')
restaurant_2 = Restaurant('Åsbro Pizzeria', 'Skabbpizza')
restaurant_3 = Restaurant('CoCo Thai', 'Thai food')

restaurant_1.set_number_served(12)
print(restaurant_1.number_served)
restaurant_1.increment_number_served(10)
print(restaurant_1.number_served)
