class Car:
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formttated name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()


my_new_car = Car('Tesla', 'road star', '2020')
print(my_new_car.get_descriptive_name())
