class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business")

restaurant = Restaurant('yellow chillies', 'african and continental')
print(f"number served: {restaurant.number_served}")
print(f"cuisine type: {restaurant.cuisine_type}")

