# class Dog:

#     def __init__(self, name, age):
#         """initialize name and age attributes"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")


# the_dog = Dog('Willie', 6)
# our_dog = Dog('Lucy', 3)

# print(f"My dog's name is {the_dog.name}.")
# print(f"My dog is {the_dog.age} years old.")

# the_dog.sit()
# the_dog.roll_over()

# print(f"our dogs name is {our_dog.name}.")
# print(f"our dog is {our_dog.age} years old.")
# our_dog.sit()
# our_dog.roll_over()

# code to print out the individual words in a sentence
sentence = input("enter the words: ")
individual_lines = sentence.split()

for lines in individual_lines:
    print(lines)
