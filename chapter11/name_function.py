def get_formatted_name(first, middle, last):
    # geerate a neatly formatted full name.
    full_name = f"{first} {middle} {last}"
    return full_name.title()


print(get_formatted_name('osasu', 'ehi', 'ogbebor'))
