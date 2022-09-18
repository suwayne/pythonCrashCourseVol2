"""
Privileges: Write a separate Privileges class. The class should have one attribute, 
privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() 
method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new 
instance of Admin and use your method to show its privileges.
"""
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



admin1 = Admin('osasu', 'ogbebor', 'male', 'nigeria', 34, ['can post', 'can delete', 'can create a user'])
admin1.privileges.show_privileges()