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
# - try
# - except
# - else
# - finally
# - raise