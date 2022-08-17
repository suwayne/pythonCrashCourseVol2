"""
Write a function that stores information about a car in a dictionary. The function should always receive 
a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the 
function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one:
"""

def make_car(manufacturer, model_name, **other_info):
    """print out details of a car"""
    other_info['make'] = manufacturer
    other_info['model'] = model_name
    return other_info

vehicle1 = make_car('nissan', 'supra', color = 'blue', tow_package = True)
print(vehicle1)
