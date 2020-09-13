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
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


iyayi = User('Iyayi', 'Ogbebor', 32, 'Feb 12')
iyayi.describe_user()

osasu = User('osasu', 'ogbebor', 32, 'september 13th')
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
print(f"{osasu.login_attempts}")

osasu.reset_login_attempts()
print(f"{osasu.login_attempts}")
