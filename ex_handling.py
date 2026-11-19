#exception is an error that lets the code stop from terminating unexpectedly
# Exception handling is a mechanism in Python used to detect and handle runtime errors 
# so that a program can execute without terminating unexpectedly.
#syntax,runtime and logical errors are the three types of errors in python
#Exception	Explanation	Example
# ZeroDivisionError	Division by zero	10 / 0
# ValueError	Correct type but invalid value	int("hello")
# TypeError	Incompatible data types	"10" + 5
# IndexError	Invalid list index	list[10]
# KeyError	Missing dictionary key	dict["age"]
# NameError	Variable not defined	print(x)
# FileNotFoundError	File does not exist	Opening a missing file
# ImportError	Import cannot be completed	Missing imported name
# Python provides five important keywords:
# - try :contains statements that might generate an exception during execution.
# (a try block needs an except or finally block to form a complete exception-handling structure)
# - except :handles the exception if it occurs.
# - else :executed if no exception occurs.
# - finally :executed regardless of whether an exception occurs or not.
# - raise :used to throw a custom exception.

#if you enter a non-integer value, the program will raise a ValueError exception and print "Invalid input! Please enter numbers only."
try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("Invalid input! Please enter numbers only.")

#else block is executed if no exception occurs in the try block
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print("You entered:", num)
    print("Conversion successful!")

#raise exception is used to throw a custom exception. It allows you to create your own error messages and handle specific situations in your code.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
try:
    print(divide(10, 0))

except ZeroDivisionError as e:
    print(e)
#or

age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("You must be 18 or older!")

print("You are eligible!")


#multiple exception handling is used to handle different types of exceptions that may occur in a try block.
#  It allows you to specify multiple except blocks, each targeting a specific exception type, enabling more precise error
#  handling and providing appropriate responses based on the nature of the exception encountered.
