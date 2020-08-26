class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Welcome to {self.restaurant_name} and we serve freshly made {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open for orders.")


restaurant = Restaurant('Sweet Sensation', 'urban')
