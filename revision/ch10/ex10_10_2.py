"""
Combine the two programs from Exercise 10-11 into one file. If the 
number is already stored, report the favorite number to the user. If 
not, prompt for the users favorite number and store it in a file. Run the program 
twice to see that it works.
"""

import json

filename = 'invite_list.json' 

with open(filename) as f: 
    rsvp = json.load(f)

print(rsvp)

