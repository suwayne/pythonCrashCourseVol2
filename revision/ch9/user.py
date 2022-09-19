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

class Admin(User):
    def __init__(self, first_name, last_name, sex, country, age, privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.country = country
        self.age = age
        self.privileges = Privileges(privileges)

    def display_privileges(self):
        print("Your privileges are:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        """display privileges"""
        print('privileges:')
        for privilege in self.privileges:
            print(f"- {privilege}")