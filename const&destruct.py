# Constructor: Used to initialize an object when it is created.
# Destructor: Used for cleanup when an object is being destroyed or finalized.
# In Python, __init__() is commonly called the constructor, although technically it is an initializer. 
# The actual object creation is handled by __new__().
# class defines a class.
# __init__() is the initializer method.
# self refers to the current object.
# It executes automatically when an object is created.
#types:
# Default / Non-parameterized constructor:
# A constructor that does not accept additional arguments apart from self.
class Student:

    def __init__(self):
        self.name = "Umra"
        self.age = 22
        self.course = "MCA"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


s1 = Student()
s1.display()


