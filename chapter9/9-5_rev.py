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

    def count_logins(self):
        print(
            f"The user {self.first_name} has logged in {self.login_attempts} times.")


osasu = User('osasumwen', 'ogbebor', 32, 'july 2020')
osasu.describe_user()

osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.count_logins()
