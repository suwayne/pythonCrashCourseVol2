# def get_formatted_name(first, last):
#     """generate a neatly formateed name"""
#     full_name = f"{first} {last}"
#     return full_name.title()


def get_formatted_name(first, last, middle=''):
    """generate a neatly formateed name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    
    else:       
        full_name = f"{first} {last}"
    return full_name.title()

