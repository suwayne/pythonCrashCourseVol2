from user_98 import User


class Admin(User):
    def __init__(self, first_name, last_name, age, signup_date):
        super().__init__(first_name, last_name, age, signup_date)
        """making the privileges instance an attribute in the admin class."""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        # print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"{privilege}")
        else:
            print("- This user has no privileges.")
