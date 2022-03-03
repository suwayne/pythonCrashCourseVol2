# programming poll
filename = 'programming_poll.txt'

print("Enter quit when you are finished.")

while True:
    name = input('Why do you like programming?: ')
    if name == 'quit':
        break

    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
        print(f"Hello {name.title()} you have been added to the guest book.")
