"""
An administrator is a special kind of user. Write a class called Admin that inherits from 
the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings 
like "can add post", "can delete post", "can ban user", and so on. Write a method called 
show_privileges() that lists the administrators set of privileges. Create an instance of Admin, 
and call your method.
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
        super().__init__(first_name, last_name, sex, country, age)
        self.privileges = privileges

    def display_privileges(self):
        print("Your privileges are:")
        for privilege in self.privileges:
            print(f"- {privilege}")

standard_user = Admin('osasu', 'ogbebor', 'male', 'nigeria', 34, 'admin')
standard_user.describe_user()

standard_user.privileges =[
    'cannot reset password',
    'can sign in',
    'can suspend personal account',
]
standard_user.display_privileges()
