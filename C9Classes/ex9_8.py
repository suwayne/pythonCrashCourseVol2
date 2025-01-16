"""
Write a separate Privileges class. The class should have one attribute, privileges, that 
stores a list of strings as described in Exercise 9-7. Move the show_privileges() method 
to this class. Make a Privileges instance as an attribute in the Admin class. Create a new 
instance of Admin and use your method to show its privileges.
"""
class User:

    def __init__(self, first_name, last_name, age, signup_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.signup_date = signup_date

    def describe_user(self):
        """summary of the user's information"""
        print(
            f"The user {self.first_name} {self.last_name} is {self.age} years old and signed up on {self.signup_date}")

class Admin(User):
    """inherinting from User class"""

    def __init__(self, first_name, last_name, age, signup_date, privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.signup_date = signup_date
        self.privileges = privileges
    
    def show_privileges(self):
        """this stores a list of strings"""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_1 = Admin('osasu', 'ogbebor', 34, 'april 28', ['can add post', 'can delete post', 'can ban user'])
admin_1.show_privileges()