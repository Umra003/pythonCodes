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


# Parameterized constructor:
# A constructor that accepts additional parameters to initialize an object with user-supplied values.
class BankAccount:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


a1 = BankAccount("Umra", 101, 5000)
a2 = BankAccount("Ayesha", 102, 10000)

a1.display()

print("----------------")

a2.display()


#note:Python does not support multiple __init__() methods through traditional constructor overloading. 
# If you define __init__() twice in the same class, the second definition replaces the first. You can use default arguments to achieve similar flexibility.
