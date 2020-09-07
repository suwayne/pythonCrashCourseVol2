class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business.")

    def customers_fed(self):
        print(f"number of customers served: {self.number_served}")

    def set_number_served(self, number_served):
        self.number_served = number_served


restaurant = Restaurant('dominos', 'pizza')
restaurant.customers_fed()
