# x ="pranjal"
# print(type(x))

class Person:
    def __init__(self, name = "Rahul", age=25):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is", self.name)
    def get_age(self):
        return self.age
# Creating objects (instances) of the class
person= Person()
person.greet()
person1 = Person("John", 25)
person2 = Person("Alice", 30)
person3 = Person("Pranjal",30)
# Accessing object attributes
print(person1.name) # Output: John
print(person2.get_age()) # Output: 30
# Invoking object methods
person1.greet() # Output: Hello, my name is John
person2.greet() # Output: Hello, my
person3.greet()
my_list = list (range(1,10))