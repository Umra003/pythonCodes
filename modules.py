# A module is simply a Python file that contains reusable code, such as functions, variables and classes.

# Instead of writing the same code again and again, we can create a module and use it whenever needed.
#types: built-in modules, third-party modules, user-defined modules
# Built-in modules: These are the modules that come pre-installed with Python. Examples include math, os, sys, random, datetime, etc.
# Third-party modules: These are the modules that are developed by the Python community and can be installed using package managers like pip.
#  Examples include NumPy, Pandas, Requests, Flask, Django, etc.
# User-defined modules: These are the modules that are created by users to organize their code into separate files.
#  Users can create their own modules by writing Python code in a .py file and importing it into other scripts.

#1. Built-in modules: These are the modules that come pre-installed with Python.
import math
#min(),max(),sum(),abs(),round(),sorted(),type() are built-in functions that are always available in Python.No need to import any module to use them.
print(math.sqrt(25))       # Square root
print(math.factorial(5))   # Factorial
print(math.pow(2, 3))      # Power
print(math.ceil(4.2))      # Round up
print(math.floor(4.8))     # Round down
print(math.pi)             # Pi

# random Module
# Used to generate random numbers or select random items.
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Randomly select an item from a sequence(list, tuple, or string)
print(random.random())  # Random float between 0.0 and 1.0
numbers = [1, 2, 3, 4, 5]# shuffle the list of numbers
random.shuffle(numbers)
print(numbers)


#datetime Module
# Used to work with dates and time.
import datetime
now = datetime.datetime.now()  # Current date and time
print(now)  # Print the current date and time
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
today = datetime.date.today()  # Current date
print(today)  # Print the current date
timedelta = datetime.timedelta(days=7)  # Time difference of 7 days
next_week = today + timedelta  # Date after 7 days
print(next_week)  # Print the date after 7 days

#user-defined modules:
# A user-defined module is a Python file created by the programmer to store reusable code such as:
# - Functions
# - Variables
# - Classes
import mymodule #Imports our Python file i.e mymodule.
print(mymodule.add(10, 20))
print(mymodule.sub(20, 5))
print(mymodule.name)
print(mymodule.college)
print(mymodule.year)
mymodule.greet()
#different ways to import a module:
#1. import module_name
#eg: import mymodule
#2. from module_name import function_name
#eg: from mymodule import add
#3. from module_name import function_name as alias
#eg: from mymodule import add as addition
#4. import module_name as alias
#eg: import mymodule as mm