# In Python, both self and cls are used inside class methods, but they refer to different things.

# 1. self – Refers to the current object
# - self represents the object that is currently being used.
# - It is used inside instance methods.
# - It helps us access or modify the data belonging to a particular object.
# - Every object can have different values for its instance variables.
# Example: If we create two student objects, s1 and s2, each student can have a different name and age. 
# We use self to access that particular student's information.

# 2. cls – Refers to the current class
# - cls represents the class itself, not an individual object.
# - It is used inside class methods.
# - It helps us access or modify class variables, which are shared by objects of that class.
# - A class method is defined using the @classmethod decorator.
# Example: Suppose all students belong to the same college, IMCC.
#  If we change the college name using cls, the updated class-level value can be shared by all student objects.

class Student:

    college = "IMCC"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", self.college)

    # Class method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name


s1 = Student("Umra", 22)
s2 = Student("Ayesha", 21)

s1.display()
s2.display()

print("---- Changing College ----")

Student.change_college("Modern College")

s1.display()
s2.display()



#using cls:
class Student:
    college = "IMCC"

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name


s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)

Student.change_college("Modern College")

print(s1.college)
print(s2.college)