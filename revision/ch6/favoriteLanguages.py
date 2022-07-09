
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

#looking up the favorite language of one of the people that took the poll:
language = favorite_languages['edward'].title()

print(language)

for name, language in favorite_languages.items():
    print(f"{name.title()}s favorite programming language is: {language}.")
    

