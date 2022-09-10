"""
Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method.
"""
class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business.")

class IceCreamStand(Restaurant):
    """A simple ice cream stand (inheriting from restaurant class)."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavor(self):
        """Display ice cream flavor"""
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")
        

ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['chocolate', 'banana'])
ice_cream.display_flavor()
