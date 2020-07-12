class User():
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        msg = f"{self.first_name} is from the {self.last_name} clan, {self.age} years old and {self.height} tall"
        print(f"\n{msg}")
