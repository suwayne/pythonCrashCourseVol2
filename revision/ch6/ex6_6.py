# Loop through the list of people who should take the poll. If they have already taken the poll, 
# print a message thanking them for responding. If they have not yet taken the poll, print a message 
# inviting them to take the poll.

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

#making a list of people who should have taken the poll.
pollers =  ['victor', 'edward', 'james', 'phil', 'percy']

#looking up the favorite language of one of the people that took the poll:
language = favorite_languages['edward'].title()

# print(language)

for name, language in favorite_languages.items():
    print(f"{name.title()}s favorite programming language is: {language.title()}.")


