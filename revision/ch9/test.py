class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking')

    def speak(self):
        print('hello my name is ' + self.name + ' and i am ' + self.age + ' years old.')


    
john = Person('john', '22')
# print(john.name)
john.speak()
john.walk()

mariam = Person('marian', '18')
mariam.speak()
mariam.walk()

