class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """set odometer to a given value"""
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback an odometer.")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """print a statement describing battery size."""
        print(f"This car has a {self.battery_size}-Kwhs battery")

    def fill_gas_tank(self):
        """electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar('tesla', 'model s', '2019')

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
