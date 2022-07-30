responses = {}

#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store the response in the dictionary
    responses[name] = response

    #find out if anyone else will take the poll
    repeat = input("Would you like to let another person respond? (yes/ no): ")
    if repeat == 'no':
        polling_active = False
    
    #polling is complete. show the results
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

    
