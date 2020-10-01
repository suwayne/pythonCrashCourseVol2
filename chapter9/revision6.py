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
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = [
            'berry triffidy',
            'tresticular berry',
            'bet on the berries'
        ]

    def display_flavours(self):
        print(f"The flavours available are {self.flavours}")


waynes_rolls = IceCreamStand('wayne rolls', '')
waynes_rolls.display_flavours()
