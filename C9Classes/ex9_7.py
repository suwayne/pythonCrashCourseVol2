"""
An administrator is a special kind of user. Write a class called Admin that inherits from the User 
class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on. Write a method 
called show_privileges() that lists the administrators set of privileges. Create an instance of Admin, 
and call your method.
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