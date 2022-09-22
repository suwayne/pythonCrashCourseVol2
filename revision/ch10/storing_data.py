"""number_writer.py"""
# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = 'numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)


"""#remember_me.py"""
# import json

# username = input("what is your name? ")
# filename = "username.json"
# with open(filename, "w") as f:
#     json.dump(username, f)
#     print(f"we'll remember you when you come back, {username}.")

"""
noting down the steps:
1. import the json module
2. create a file 'username.json' and store it in the filename variable
3. open the file with the 'w' flag, give it an alias f
4. dump the input in the file you've created and aliased as f.
5. print a custom message.
"""

"""greet_user.py"""
import json

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"welcome back {username}!")

