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

    def customers_served(self, number_served):
        print(f"{self.number_served} customers have been served.")

    def set_number_served(self, number_served):
        "allow user to set the number of customers served."
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        "allow incrementation on number of customers served"
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """represent an ice cream stand"""

    def __init__(self, name, cuisine_type='ice_cream'):
        """initialize the attributes from the parent class"""
        super().__init__(name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        """Display the flavours available."""
        print("\nWe have the following flavours available:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")
