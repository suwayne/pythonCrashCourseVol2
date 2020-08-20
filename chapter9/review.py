class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}."
        return long_name.title()


my_new_car = Car('BMW', '3i', '2018')
print(my_new_car.get_descriptive_name())
