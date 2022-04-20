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


class IceCreamStand(Restaurant):
    """A class to model an ice cream stand list based on the restaurant list"""

    def describe_restaurant(self):
        """Prints a description of the ice cream stand."""
        print(f"{self.restaurant_name} is an ice cream stand that serves {self.cuisine_type}.")

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)

    def get_flavors(self):
        flavors = ['strawberry', 'blueberry', 'vanilla', 'chocolate', 'banana split']
        print(f"{self.restaurant_name.title()} has the following flavors:")
        for flavor in flavors:
            print(f"\t***{flavor.title()}***")


restaurant_1 = Restaurant('Svarta Pannan', 'Husmanskost')
restaurant_2 = Restaurant('Åsbro Pizzeria', 'Skabbpizza')
restaurant_3 = Restaurant('CoCo Thai', 'Thai food')
restaurant_4 = IceCreamStand('Börjes Glass', 'Ice cream')

IceCreamStand.describe_restaurant(restaurant_4)
Restaurant.open_restaurant(restaurant_4)
restaurant_4.get_flavors()
