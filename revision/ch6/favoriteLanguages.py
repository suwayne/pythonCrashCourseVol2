
# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }

#looking up the favorite language of one of the people that took the poll:
# language = favorite_languages['edward'].title()

# print(language)

# for name, language in favorite_languages.items():
#     print(f"{name.title()}s favorite programming language is: {language}.")

#looking up the favorite language of one of the people that took the poll:
# language = favorite_languages['edward'].title()

# print(language)

# for name, language in favorite_languages.items():
#     print(f"{name.title()}s favorite programming language is: {language}.")
    


    
"""
modifying the favorite languages syntax with a dictionary that's got list as its value in the key value string.
"""


favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, languages in favorite_languages.items():
       print(f"\n{name.title()}'s favorite languages are:")
       for language in languages:
              print(f"\t{language.title()}")


