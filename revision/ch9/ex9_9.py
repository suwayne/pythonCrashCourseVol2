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


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 200:
            range = 315
        print(f"This car can go about {range} range in a full charge.")
    
    def upgrade_battery(self):
        """check capacity size and upgrade it to 100"""
        if self.battery_size != 100:
            self.battery_size = 150


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """initialize attriutes of the parent class."""
        super().__init__(make, model, year)
        """tells python to create a new instance of battery with a default size of 75"""
        self.battery = Battery()

    def fill_gas_tank(self):
        """electric car's dont have gas tanks"""
        print("This car doesn't need a gas tank!")




my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()