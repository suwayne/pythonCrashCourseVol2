class User():
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.height = height

    def describe_user(self):
        msg = f"{self.first_name} is from the {self.last_name} clan, {self.age} years old and {self.height} tall"
        print(f"\n{msg}")

    def greet_user(self):
        msg = f"How are you doing today {self.first_name} {self.last_name}."
        print(f"\n{msg}")


iyayi = User('iyayi', 'ogbebor')
iyayi.greet_user()
