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

french_restaurant = Restaurant('le bonbon', 'european & continental')
german_restaurant2 = Restaurant('donner kebab', 'wraps & fast food')
nigerian_restaurant3 = Restaurant('mr biggs', 'african styled fast food')


french_restaurant.describe_restaurant()
french_restaurant.open_restaurant()
print("---")
german_restaurant2.describe_restaurant()
german_restaurant2.open_restaurant()
print("---")
nigerian_restaurant3.describe_restaurant()
nigerian_restaurant3.open_restaurant()

