"""
Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, 
and they clarify the role of each value in the function call.
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type};")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')       #you're calling the function and ensuring the right arguments are 
                                                            #assigned using the keyword arguments


#personal practice with 3 parameters
# def describePet(name, breed, age):
#     """a little practice here"""
#     print(f"My pets name is {name}, and it's a {breed} breed and will turn {age} this year.")
    
# describePet(age = 8, name ='rocky', breed = 'gsd')
