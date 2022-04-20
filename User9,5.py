class Users:
    """A class to model a user profile list"""

    def __init__(self, first_name, last_name, username, age, password):
        """Initialized the first_name, last_name, username, age and password attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Prints all information about the user."""
        print(f"\nUser: {self.username}'s name is {self.first_name} {self.last_name}. ")
        print(f"He/she is {self.age} years old and has '{self.password}' as his/her password.")

    def greet_user(self):
        """Prints a default greeting to the user."""
        print(f"Hello, {self.first_name}! Have a good day!")

    def increment_login_attempts(self, attempt):
        """Increments the number of login attempts."""
        if attempt >= 0:
            self.login_attempts += attempt
        else:
            print("You can't decrease the amount of login attempts.")

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = Users('Borrskaft', 'McFeastsson', 'donkelidonk', 63, 'böööööörje!!!')
user_2 = Users('Lars', 'Dönersås', 'LarsBerit', 72, 'smör')
user_3 = Users('Agda', 'Blomkålsson', 'blommis', 91, 'password')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_3.increment_login_attempts(1)
print(user_3.login_attempts)
user_3.increment_login_attempts(2)
print(user_3.login_attempts)
user_3.increment_login_attempts(7)
print(user_3.login_attempts)
user_3.reset_login_attempts()
print(user_3.login_attempts)
