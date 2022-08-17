"""
Each instance created from the Dog class will store a name and an age, and well 
give each dog the ability to sit() and roll_over():
"""

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def span(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is {self.age} years old!")


breed_1 = Dog('rocky', 12)

#these two are the same
print(breed_1.sit())
breed_1.sit()

# print(breed_1.span())




