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

    def set_number_served(self, number_served):
        """Allow a user to set the number of users that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment number of customers served"""
        self.number_served += additional_served


# creating an instance 'restaurant' from my class
restaurant = Restaurant('Dominos', 'Pizza')
restaurant.describe_restaurant()

print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(6669)
print(f"Number served: {restaurant.number_served}")
