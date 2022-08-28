class User:
    def __init__(self, first_name, last_name, sex, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.country = country
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()} we know you are a {self.age} {self.sex} living in {self.country}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome onboard")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


    
user1 = User('osasu', 'ogbebor', 'male', 'nigeria', '34')

user1.describe_user()
user1.greet_user()

iyayi = User('iyayi', 'ogbebor', 'female', 'usa', 29)

iyayi.describe_user()
iyayi.greet_user()

print(f"number of login attempts by yayi: " + str(iyayi.login_attempts))

iyayi.increment_login_attempts()
print(f"number of login attempts by yayi: " + str(iyayi.login_attempts))

iyayi.reset_login_attempts()
print(f"number of login attempts by yayi: " + str(iyayi.login_attempts))
