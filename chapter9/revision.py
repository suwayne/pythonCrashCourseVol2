# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(
#             f"Welcome to {self.restaurant_name} and we serve freshly made {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} restaurant is open for orders.")


# restaurant = Restaurant('Sweet Sensation', 'urban')
# restaurant.describe_restaurant()

# mainland = Restaurant('Mr Biggs', 'Fast food')
# mainland.describe_restaurant()
# mainland.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old, and works as a {self.profession.title()}.")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")


suwayne = User('Osasu', 'ogbebor', 32, 'security engineer')
suwayne.describe_user()
suwayne.greet_user()
