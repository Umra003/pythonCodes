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

# Multiple Inheritance
# Definition: When one child class inherits from two or more parent classes, it is called Multiple Inheritance.
class Father:
    def skills1(self):
        print("Father: Driving")

class Mother:
    def skills2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skills3(self):
        print("Child: Painting")

# Creating object
c = Child()

c.skills1()
c.skills2()
c.skills3()

# Multilevel Inheritance
# Definition: When a class inherits from another child class, forming a chain of inheritance, it is called Multilevel Inheritance.
class Grandfather:
    def house(self):
        print("Grandfather owns a house")

class Father(Grandfather):
    def car(self):
        print("Father owns a car")

class Son(Father):
    def bike(self):
        print("Son owns a bike")

# Creating object
s = Son()

s.house()
s.car()
s.bike()