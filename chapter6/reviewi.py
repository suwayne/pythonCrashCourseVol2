# # starting with an emty dictionary
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# alien_0['speed'] = 'fast'
# print(alien_0)
# print("original x-position: " + str(alien_0['x_position']))

# # move the alien to the right
# # determine how far to move the alien based on its current speed

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("new x-position: " + str(alien_0['x_position']))

# removing key value pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("sarah's favorite language is " + favorite_languages['sarah'])

# looping through all key-value pairs
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(key + ": " + value)
# print("\n key:" + key)
# print("value:" + value)

# favorite languages

# looping through all keys in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
#     else:
#         print("Obviosly " + name.title() + " does not like to code.")

# looping through all values in a dictionary
print("the following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language)

for language in set(favorite_languages.values()):
    print(language.title())

print("...")

# fav = list(set(favorite_languages))
# print(fav)
