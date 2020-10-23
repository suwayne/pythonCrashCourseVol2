import json


def get_stored_user_name():
    # get stored username if available.
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None
    else:
        return username


def get_new_user_name():
    # prompt for a new user name
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_user_name()

    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"welcome back, {username}")

    else:

        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back {username}")


greet_user()
