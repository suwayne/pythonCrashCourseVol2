
def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()    #return will break you out of the function; a print statement wont work after you use return.



musician = get_formatted_name('jimi', 'hendrix')
print(musician)



