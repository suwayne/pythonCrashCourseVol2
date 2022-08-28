from ast import Return


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business")

    def set_number_served(self, number_served):
        """Allow users to set the number of customers that have been served"""
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served



restaurant = Restaurant('mr biggs', 'fast food')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))

#setting the ammount of served customers using "self.number_served" before printing the result
restaurant.number_served = 3000
print("\nNumber served: " + str(restaurant.number_served))

restaurant.increment_number_served(5000)
print("\nNumber served: " + str(restaurant.number_served))

