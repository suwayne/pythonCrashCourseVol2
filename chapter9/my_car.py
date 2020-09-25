# if you are going to import and use your class as an alias
from electric_car import Car as CA
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


osasu_car = CA('audi', 'a7', 2020)
print(osasu_car.get_descriptive_name())
