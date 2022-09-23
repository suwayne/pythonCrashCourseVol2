# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(self.name + ' is walking')

#     def speak(self):
#         print('hello my name is ' + self.name + ' and i am ' + self.age + ' years old.')


    
# john = Person('john', '22')
# # print(john.name)
# john.speak()
# john.walk()

# mariam = Person('marian', '18')
# mariam.speak()
# mariam.walk()


# file_name = "new_guest.txt"

# prompt = input("what is your name?: ")
# with open(file_name, 'a') as f:
#     f.write(f"{prompt}\n")

import json
stored_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
file = 'stored_num.json'

with open(file, 'a') as f:
    json.dump(stored_num, f)
