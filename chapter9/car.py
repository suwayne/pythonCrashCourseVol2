class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
        # print(f"\n{long_name.title()}")

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # def update_odometer(self, mileage):
    #     """set the odometer reading to the given value"""
    #     self.odometer_reading = mileage

    def update_odometer(self, mileage):
        """set the odometer reading to the given value
           Reject the change if it attempts to roll the odometer
           back        
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()
