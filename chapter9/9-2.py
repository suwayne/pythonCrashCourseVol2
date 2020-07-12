class Restaurant():
    # lil hint to remember: by standard Classes are capitalized
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.restaurant_name} is open, please come in."
        print(f"\n{msg}")


suwayne = Restaurant('waynes bistro', 'sandwiches')
suwayne.describe_restaurant()

love = Restaurant('frozen rolls', 'ice cream')
love.describe_restaurant()

osasu = Restaurant('hop and hop', 'pancakes')
osasu.describe_restaurant()
