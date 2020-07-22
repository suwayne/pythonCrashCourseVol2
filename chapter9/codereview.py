class Restaurant():
    # lil hint to remember: by standard Classes are capitalized
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        msg = (f"{self.restaurant_name} serves wonderful {self.cuisine_type}.")
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.restaurant_name} is open, please come in."
        print(f"\n{msg}")


# creating an instance 'restaurant' from my class
restaurant = Restaurant('Dominos', 'Pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
