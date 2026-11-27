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

# MRO stands for Method Resolution Order.(multiple inheritance)(order matters)
# MRO is the order in which Python searches for a method or attribute in a class and its parent classes.
# Suppose a child class inherits from two parent classes, and both parents have a method with the same name.
# When we call that method using the child object, which parent's method should Python execute?
# To decide this, Python follows a specific searching order called MRO.
class Father:
    def show(self):
        print("Father's method")

class Mother:
    def show(self):
        print("Mother's method")

class Child(Father, Mother):
    pass

c = Child()
c.show() #this will print "Father's method" because Father is listed first in the inheritance list of Child class. If we change the order to class Child(Mother, Father), it will print "Mother's method".
# using the MRO, we can also check the order in which Python searches for methods in a class hierarchy. We can use the mro() method or the __mro__ attribute to see the MRO of a class.
# in multiple inheritance, super() means:
# Go to the next class in the MRO order.
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):#order matters
    def show(self):
        print("D")
        super().show()

d = D()
d.show()

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

# Hierarchical Inheritance
# Definition: When two or more child classes inherit from the same parent class, it is called Hierarchical Inheritance.
class Employee:
    def company(self):
        print("Working in ABC Company")

class Manager(Employee):
    def manage(self):
        print("Manager manages the team")

class Developer(Employee):
    def coding(self):
        print("Developer writes code")

# Creating objects
m = Manager()
d = Developer()

m.company()
m.manage()

d.company()
d.coding()


# Hybrid Inheritance
# Definition: When two or more different types of inheritance are combined in a single program, it is called Hybrid Inheritance.
class A:
    def display(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def print_data(self):
        print("Class C")

class D(B, C):
    def output(self):
        print("Class D")

# Creating object
d = D()

d.display()
d.show()
d.print_data()
d.output()