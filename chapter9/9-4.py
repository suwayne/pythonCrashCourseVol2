# number served
class Restaurant():
    # lil hint to remember: by standard Classes are capitalized
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = (f"{self.restaurant_name} serves wonderful {self.cuisine_type}.")
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.restaurant_name} is open, please come in."
        print(f"\n{msg}")

    def number_served(self, additional_served):
        """allow user to increment no. of customers served."""
        self.number_served += additional_served


# creating an instance 'restaurant' from my class
# restaurant = Restaurant('Dominos', 'Pizza')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant = Restaurant('suwayne sandwiches', 'sandwiches')
restaurant.describe_restaurant()
restaurant.number_served()
# ..more syntx cooking...
