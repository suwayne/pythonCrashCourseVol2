class User():

    def __init__(self, first_name, last_name, age, height, login_attempts):
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
        """Increment the value of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset the value of login attempts to 0"""
        self.login_attempts = 0


iyayi = User(Iyayi, Ogbebor, 27, 170, 4)
iyayi.increment_login_attempts()
