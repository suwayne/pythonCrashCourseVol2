def get_formatted_name(first_name, last_name):
    # return a full name, neatly formatted
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# this is an infinite loop
while True:
    print("\nplease tell me your name:")
    f_name = input("enter your first name: ")
    l_name = input("enter your last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)
