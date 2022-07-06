current_users = ["iyayi", "osita", "morakinyo", "joshua", "ghome"]
new_users = ["iyayi", "joshua", "dami", "sagir", "chidera"]

for new_user in new_users:
    if new_user in current_users:
        print(f"the username {new_user} is available.")
    else:
        print("you will need to enter a new username.")
        

######## here's the solution i found on reddit.

# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"Sorry {new_user}, that name is taken.")
#     else:
#         print(f"Great, {new_user} is still available.")