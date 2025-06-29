
# Write a Python program that demonstrates the use of inheritance in object-oriented programming (OOP). The program should have three classes:
# Animal: The base class with a method speak() that prints "Animal Speaking".
# Dog: A child class that inherits from the Animal class and has an additional method bark() that prints "Dog Barking".
# DogChild: A grandchild class that inherits from the Dog class and has an additional method eat() that prints "Eating bread...".

class Animal:

    def speak(self):
        print("Animal speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


class DogChild(Dog):
    def eat(self):
        print("Eating bread")


d = Animal()
d.speak()

germansheperd = Dog()
germansheperd.bark()

puppy = DogChild()
puppy.eat()