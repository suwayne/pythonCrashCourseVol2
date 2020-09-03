class User:
    def __init__(self, first_name, last_name, age, signup_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.signup_date = signup_date
        self.login_attempts = 0

    def describe_user(self):
        """summary of the user's information"""
        print(
            f"The user {self.first_name} {self.last_name} is {self.age} years old and signed up on {self.signup_date}")

    def increment_login_attempts(self):
        "increment login attempts by 1 and add it to self.login_attempts()"
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset login attempts to o"""
        self.login_attempts = 0


"""an instance of the class User"""
iyayi = User('Iyayi', 'Ogbebor', 32, 'Feb 12')
iyayi.describe_user()

print(f"Number of login attempts:")
iyayi.increment_login_attempts()
iyayi.increment_login_attempts()
iyayi.increment_login_attempts()
print(f"{iyayi.login_attempts}")


print(f"resetting login attempts")
iyayi.reset_login_attempts()
print(f"{iyayi.login_attempts}")
