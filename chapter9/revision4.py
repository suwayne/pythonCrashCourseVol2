class Car:
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        """creating a value for odometer_reading without passing it into the init method"""
        self.odometer_reading = 200

    def get_descriptive_name(self):
        """return a neatly formttated name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the mileage on the car"""
        print(f"The car has a mileage of {self.odometer_reading}")

    """modifying the odometer_reading value with a method"""

    def update_odometer(self, mileage):
        """set the odometer to the mileage value"""
        self.odometer_reading = mileage


my_new_car = Car('Tesla', 'road star', '2020')
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

print("The new mileage reading:")
my_new_car.update_odometer(3000)
my_new_car.read_odometer()
