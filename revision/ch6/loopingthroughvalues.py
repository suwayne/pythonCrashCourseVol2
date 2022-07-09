#looping through values in a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("the following languages have been mentioned in the poll:")
# for value in favorite_languages.values():   #at this point i'm gaining mastery of how to use methods and functions. 
#     print(value)

#to print out the values without repetition(python is repeated in this case, we use the set function.)
for value in set(favorite_languages.values()):
    print(value)

#as you can see the set function prevents duplication.
