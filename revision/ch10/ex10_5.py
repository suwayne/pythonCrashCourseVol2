"""
Write a while loop that asks people why they like programming. Each time 
someone enters a reason, add their reason to a file that stores all the responses.
"""
filename = 'whyDoYouCode.txt'

while True:
    question = input('Enter quit to end this!\nWhy do you like programming?: ')
    print('Enter quit to close this program')
    if question == 'quit':
        break
    else:

        with open(filename, 'a') as file_object:
            file_object.write(f"{question}\n")

            

