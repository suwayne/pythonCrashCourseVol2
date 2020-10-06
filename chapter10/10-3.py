filename = 'guest.txt'

prompt = 'what is your name?: '

response = input(prompt)

with open(filename, 'a') as file_object:

    file_object.write(response.title())
