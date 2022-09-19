class User:
    def __init__(self, first_name, last_name, sex, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.country = country
        self.age = age
    
    def describe_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()} we know you are a {self.age} {self.sex} living in {self.country}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome onboard")