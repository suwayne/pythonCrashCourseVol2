"""
working with a default value as a parameter, and assigning arguments to a parameter
"""

def describe_pet(breed, animal_type = 'dog'):
    """defining do with default value for its parameter"""
    print(f"I own a {animal_type}")
    print(f"My house pet is a {animal_type} and it's breed is {breed}")

describe_pet('dalmatian')

#alternatively:
# describe_pet(breed='dalmatian')


