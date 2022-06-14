# guest_list = []
# guest_list.append('mandela')
# guest_list.append('michael jackson')
# guest_list.append('tu pac')

# print(guest_list)

# print('\nhi ' + guest_list[0] + ' you are invited to dinner')
# print('hi ' + guest_list[1] + ' you are invited to dinner')
# print('hi ' + guest_list[2] + ' you are invited to dinner')

# print('\nWe are sorry to announce that ' +
#       guest_list[0] + ' wont be able to make it.')

# guest_list[0] = 'bob marley'
# print(guest_list)

# print('\nhi ' + guest_list[0] + ' you are invited to dinner')
# print('hi ' + guest_list[1] + ' you are invited to dinner')
# print('hi ' + guest_list[2] + ' you are invited to dinner')

# print('\nHi everyone we have a bigger dinner table, so we will be inviting more attendees')

# guest_list.insert(0, 'goldie')
# print(guest_list)

# guest_list.insert(2, 'fela kuti')
# print(guest_list)

# guest_list.append('chester')
# print(guest_list)


guestList = ['steve jobs', 'elijah', 'dad']

print(f"Hi {guestList[0]}, you're invited to dinner")
print(f"Hi {guestList[1]}, you're invited to dinner")
print(f"Hi {guestList[2]}, you're invited to dinner")

#changing the guest list

absentee = guestList.pop(0)
print(f"we are sad to announce that {absentee} will not be making it to the event.")

guestList.append('seyi nayin')

print(f"Hi {guestList[0]}, you're invited to dinner")
print(f"Hi {guestList[1]}, you're invited to dinner")
print(f"Hi {guestList[2]}, you're invited to dinner")


print (f"hi everyone, happy to announce that we have found a bigger venue for the event")

guestList.insert(1, 'joshua uko')

print(guestList)
