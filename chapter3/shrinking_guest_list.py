guest_list = []
guest_list.append('mandela')
guest_list.append('michael jackson')
guest_list.append('tu pac')

print(guest_list)

print('\nhi ' + guest_list[0] + ' you are invited to dinner')
print('hi ' + guest_list[1] + ' you are invited to dinner')
print('hi ' + guest_list[2] + ' you are invited to dinner')

print('\nWe are sorry to announce that ' +
      guest_list[0] + ' wont be able to make it.')

guest_list[0] = 'bob marley'
print(guest_list)

print('\nhi ' + guest_list[0] + ' you are invited to dinner')
print('hi ' + guest_list[1] + ' you are invited to dinner')
print('hi ' + guest_list[2] + ' you are invited to dinner')

print('\nHi everyone we have a bigger dinner table, so we will be inviting more attendees')

guest_list.insert(0, 'goldie')
print(guest_list)

guest_list.insert(2, 'fela kuti')
print(guest_list)

guest_list.append('chester')
print(guest_list)

print('\nNew information reaching us is we can only invite 2 guests for dinner.')

guest_list.pop()
print('\nsorry you wont be invited ' + guest_list.pop())
guest_list.pop()
guest_list.pop()

print(guest_list)

print("Hi " + guest_list[0] + " you're invited to the dinner.")

print(guest_list)

# remvoing last two names using del

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)
