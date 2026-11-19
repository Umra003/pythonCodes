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

try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("Invalid input! Please enter numbers only.")

