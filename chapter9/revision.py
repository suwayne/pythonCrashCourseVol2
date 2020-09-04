class User:
    def __init__(self, user_name, profession, email_address):
        self.user_name = user_name
        self.profession = profession
        self.email_address = email_address


# def describe_user(self):
#     print(f"User details:")
#     print(f"\t{self.user_name}")
#     print(f"\t{self.profession}")
#     print(f"\t{self.email_address}")


def greet_user(self):
    print(f"Hello! {self.user_name}, we are happy to have you.")


sasu = User('ehisumwen ogbebor', 'maintenance programmer', 'ehis_jr@yahoo.com')
sasu.greet_user()
