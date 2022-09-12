class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """initialize ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavor(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

frozen_rolls = IceCreamStand('frozen rolls', 'ice cream', ['banana', 'strawberry', 'orange'])
frozen_rolls.display_flavor()