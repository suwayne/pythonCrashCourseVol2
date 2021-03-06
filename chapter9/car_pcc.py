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


my_new_car = Car('BMW', '3i', '2018')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying an attributes value directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(40)
# my_new_car.read_odometer()

# my_new_car.update_odometer(300)
# my_new_car.read_odometer()

# my_new_car.update_odometer(3)
# my_new_car.read_odometer()


my_used_car = Car('Honda', 'Accord', '2008')
my_used_car.get_descriptive_name()

my_used_car.update_odometer(25_670)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
