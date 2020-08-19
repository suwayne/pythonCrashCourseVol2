class Dog:  # class
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):  # method definition
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):  # method definition
        """Simulate a roll over response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Rocky', 6)  # instance of a class

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# calling methods
my_dog.sit()
my_dog.roll_over()
