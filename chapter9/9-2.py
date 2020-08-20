class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business.")


osasu = Restaurant('chicken republic', 'healthy food')
osasu.describe_restaurant()

code_test = Restaurant('Mc. Donalds', 'Fast Food')
code_test.describe_restaurant()

iyayi = Restaurant('Strobies', 'Healthy Food')
iyayi.describe_restaurant()
