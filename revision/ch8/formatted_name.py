
# def get_formatted_name(first_name, last_name):
#     """Return full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()    #return will break you out of the function; a print statement wont work after you use return.



# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)



# #function defined with 3 parameters
# def get_formatted_name(first_name, middle_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = f"{first_name} {middle_name} {last_name}"
#        return full_name.title()



# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


#function defined with optional parameter -middle_name
def get_formatted_name(first_name, last_name,  middle_name=''):
       """Return a full name, neatly formatted."""
       full_name = f"{first_name} {middle_name} {last_name}"
       return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
musician = get_formatted_name('jimi', 'hendrix', 'swagger')
print(musician) 