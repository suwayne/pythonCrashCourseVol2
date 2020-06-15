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
