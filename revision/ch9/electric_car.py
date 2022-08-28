class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year}, {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(f"The car has {self.odometer_reading} miles on it")
    
    #modifying through a method
    # def update_odometer(self, mileage):
    #     """Set the odometer reading """
    #     self.odometer_reading = mileage

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll bock an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model v', 2022)
print(my_tesla.get_descriptive_name())

my_tesla.read_odometer()
# print(my_tesla.update_odometer(2300)) 
# print(str(my_tesla.odometer_reading))

my_tesla.increment_odometer(4000)
print(str(my_tesla.odometer_reading))

