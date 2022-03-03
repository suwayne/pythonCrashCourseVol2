"""A class that can be used to represent a car. """


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}."
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # modify an attributes value through a method
    def update_odometer(self, mileage):
        """set odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage  # assign the attribute to the 'mileage' variable
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """represent aspects of a car specific to electric vehicles"""

    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    """report the range of the car based on the battery size."""

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


osasu_tesla = ElectricCar('tesla', 'model s', 2019)
print(osasu_tesla.get_descriptive_name())

osasu_tesla.describe_battery()
osasu_tesla.get_range()
