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
    def __init__(self, first_name, last_name, age, signup_date):
        super().__init__(first_name, last_name, age, signup_date)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("The admins set of privileges are:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"{privilege}")
        else:
            print("This user has no privileges.")


osasu = Admin('osasu', 'ogbebor', 32, 'april 2020')
osasu.describe_user()

print("\nAdding privileges:")
osasu_privileges = [
    'can write',
    'can copy',
    'can delete'
]

# 1st access privileges from the Admin() class, the privileges from the Privileges() class
osasu.privileges.privileges = osasu_privileges
osasu.privileges.show_privileges()
