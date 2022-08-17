"""
Three Restaurants: Start with your class from Exercise 9-1. Create three different 
instances from the class, and call describe_restaurant() for each instance.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open for business")

restaurant = Restaurant('yellow chillies', 'african and continental')
restaurant2 = Restaurant('pizza hut', 'fast food')
restaurant3 = Restaurant('mr biggs', 'african styled fast food')


restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()