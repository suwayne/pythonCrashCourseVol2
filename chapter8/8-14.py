def make_car(manufacturer, model, **options):
    """make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        """for dictionary car_dict > option is the key, value is the value"""
        car_dict[option] = value
        return car_dict


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991,
                         color='white', headlight='popup')
print(my_old_accord)
