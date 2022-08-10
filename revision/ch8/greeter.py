def get_formatted_name(first_name, last_name):
    """Display a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("Enter q to quit at any time")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    if f_name and l_name == "":
        break


    print(f"\nHello, {formatted_name}!")
