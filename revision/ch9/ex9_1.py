"""
Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store 
two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
that prints these two pieces of information, and a method called open_restaurant() that prints a 
message indicating that the restaurant is open.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business")

restaurant = Restaurant('yellow chillies', 'african and continental')

restaurant.describe_restaurant()
restaurant.open_restaurant()
