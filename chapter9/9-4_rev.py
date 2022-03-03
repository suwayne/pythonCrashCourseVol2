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

    def people_served(self):
        print(
            f"The restaurant has served {self.number_served} customers today.")

    def set_number_served(self, servings):
        self.number_served = servings
        print(f"The number of servings today is: {self.number_served}")

    def increment_number_served(self, servings):
        self.number_served = servings + self.number_served
        print(f"The new ammount of customers served is: {self.number_served}")


July = Restaurant('waynes pancakes', 'breakfast')
# July.people_served()
July.set_number_served(49)
July.increment_number_served(10)
