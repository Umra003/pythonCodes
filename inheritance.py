# Inheritance is an OOP (Object-Oriented Programming) concept in which one class acquires the properties and methods of another class.

# In simple words, inheritance allows us to reuse the code of an existing class in a new class instead of writing the same code again.

# There are two important classes:
# 1. Parent Class (Base Class): The class whose properties and methods are inherited by another class.
# 2. Child Class (Derived Class): The class that inherits the properties and methods of the parent class.
# Types of Inheritance in Python
# Python supports five main types of inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# Single Inheritance
# Definition: When one child class inherits from only one parent class, it is called Single Inheritance.
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Creating object
d = Dog()

d.eat()
d.bark()