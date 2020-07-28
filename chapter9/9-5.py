class User():

    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        msg = f"{self.first_name} is from the {self.last_name} clan, {self.age} years old and {self.height} meters tall"
        print(f"\n{msg}")

    def greet_user(self):
        msg = f"How are you doing today {self.first_name} {self.last_name}."
        print(f"\n{msg}")

    def increment_login_attempts(self):
        # increment login attempts by 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # reset login attempts to 0
        self.login_attempts = 0


# iyayi = User('iyayi', 'ogbebor', 27, 180)
# iyayi.describe_user()
# iyayi.greet_user()

osasu = User('osasu', 'ogbebor', 32, 200)
print("\nMaking 3 login attempts:")
osasu.increment_login_attempts()
osasu.increment_login_attempts()
osasu.increment_login_attempts()
print(f"Login attempts: {osasu.login_attempts}")


print("\nRecheck number of login attempts after reset:")
osasu.reset_login_attempts()
print(f"Login attempts: {osasu.login_attempts}")
