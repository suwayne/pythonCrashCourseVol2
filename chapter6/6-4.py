# glossary = {
#     'dictionary': 'consists of key value pairs',
#     'lists': 'stores multiple values',
#     'variable': 'stores an items value',
#     'integer': 'a kind of datatype consisting of numbers',
#     'string': 'a kind of integer consisting of a combination of characters',
#     'boolean': 'data type representing true or false logic',
#     'set method': 'prevents repetition when looping through a dictionary',
#     'key method': 'display only keys when looping through a dictionary',
#     'item method': 'display all key, value items when looping through a dictionary',
# }

# for key, value in glossary.items():
#     print(key + ": " + value)

# rivers
# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china',
# }

# print("a little geography i never knew:")
# for river, country in rivers.items():
#     print("the " + river + " runs through " + country)

# print("\nrivers:")
# for river in rivers.keys():
#     print(river)

# print("\ncountries:")
# for country in rivers.values():
#     print(country)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

favorite_language_polls = ['sam', 'picasso',
                           'aderinsola', 'ay', 'jen', 'sarah']

for name in favorite_languages.keys():

    if name in favorite_language_polls:
        print("Thank you " + name.title() + " for responding")
    else:
        print(name.title() + " you are invited to take the poll")
