import json

# # load the username, if it has been stored previously.
# # otherwise, prompt for the username and store it.
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)

# except FileNotFoundError:

#     username = input("What is your name? ")

#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}.")
# else:
#     print(f"Welcome back {username}.")


# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)

#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"we will remember you when you come back, {username}.")

#     else:
#         print(f"welcome back, {username}!")


# greet_user()

def get_stored_user_name():
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
        print(f"welcome back, {username}")

    else:

        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back {username}")


greet_user()
