dogs = list()
dogs.append("Germany Shepard")
dogs.append("Poodle")
print(dogs)

# Dog class holds methods that should exist within object
class Dog:
    # class variables defined in class def
    # shared among all dog instances
    greeting = "Woof!"
# Initializer
# Values are called, instance variables which allows up to have unique values for each instance in which they reside.
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(self.greeting)

# must create instance of dog class to use
my_dog = Dog("Spot")
print(my_dog.name)

# Create another dog
# Dog names are instance variables
my_other_dog = Dog("Patricia")
my_other_other_dog = Dog("Greg")

print(my_other_dog.name)
print(my_other_other_dog.name)

# Make code modular
# Python provides a wy to check where code is being run with built-in variable __name__
print(__name__)
