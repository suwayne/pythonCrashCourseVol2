#glossary
glossary = {
    'data types': 'examples are integers, strings, lists, etc.',
    'if statements': 'helps you work with multiple conditions in your program',
    'f strings': 'use this with print statements to include store values in variables with your output',
    'type function': 'insert any datatype in this type() function to find out more about it',
    'dir function': 'displays details about any object you put in it',
}

for item in glossary:    #this will print out your dictionary in a neatly formatted way.
    print(item, ':\n', glossary[item], '\n')


#another way to get this done.
# for word, definition in glossary.items():
#     print(f"\n{word.title()}: {definition.title()}")


