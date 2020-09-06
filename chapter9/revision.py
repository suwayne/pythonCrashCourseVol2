class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"This is {self.first_name} {self.last_name} and is {self.age}")


iyayi = User('osasu', 'ogbebor', 32)
iyayi.describe_user()
