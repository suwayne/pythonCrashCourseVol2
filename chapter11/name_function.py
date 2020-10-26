# def get_formatted_name(first, middle, last):
#     # geerate a neatly formatted full name.
#     full_name = f"{first} {last}"
#     return full_name.title()

def get_formatted_name(first, last, middle=''):
    # generate a neatly formatted full name.
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
