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


osasu = Car('toyota', 'avalon', 2019)
print(osasu.get_descriptive_name())

# set odometer from the method, and print a statement showing the cars mileage
osasu.odometer_reading = 59
osasu.read_odometer()

# set odometer to a given value
osasu.update_odometer(3)
osasu.read_odometer()

osasu.increment_odometer(35)
osasu.read_odometer()
