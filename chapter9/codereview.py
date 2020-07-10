class Dog:

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


the_dog = Dog('Willie', 6)

print(f"My dog's name is {the_dog.name}.")
print(f"My dog is {the_dog.age} years old.")
