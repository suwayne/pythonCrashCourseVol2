def greet_users(names):
    """
    Print a simple greeting to each user in the list.
    """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margret'] 

greet_users(usernames)

#in this example we passed a list into a function.
