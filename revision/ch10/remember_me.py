import json

#Load the username, if it has been stored previously
#otherwise promt for the username and store it
# filename = "username.json"
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:

#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"we'll remember you when you come back {username}")
    
# else:
#     print(f"welcome back {username}!")

"""turning this syntax into a function"""
def greet_user():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:

        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back {username}")
        
    else:
        print(f"welcome back {username}!")

greet_user()