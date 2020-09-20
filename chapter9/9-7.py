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
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]

    def show_privileges(self):
        print(f"\nHere is a list of the Administrators privileges:")
        for privilege in self.privileges:
            print(f"-{privilege.title()}")


osasumwen = Admin('osasumwen', 'ogbebor', 32, 'april 28')
osasumwen.show_privileges()
