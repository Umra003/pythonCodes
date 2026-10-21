# The LEGB rule explains how Python searches for a variable when you use its name inside a function.
# L: Local scope
# E: Enclosing scope
# G: Global scope
# B: Built-in scope

#local scope: Variables defined inside a function are in the local scope and can only be accessed within that function.
def my_function():
    x = 10  # Local variable
    print(x)  # Accessing the local variable

#enclosing scope: Variables defined in an enclosing function can be accessed by inner functions.
def outer_function():
    x = 20  # Enclosing variable

    def inner_function():
        print(x)  # Accessing the enclosing variable

    inner_function()

#global scope: Variables defined at the top level of a script or module are in the global scope and can be accessed from anywhere in the code.
x = 30  # Global variable
print(x)  # Accessing the global variable

#built-in scope: Python has a set of built-in functions and variables that are always available. These are in the built-in scope.
print(len("Hello"))  # Using the built-in len() function
print(max(1, 2, 3))  # Using the built-in max() function
print(min(1, 2, 3))  # Using the built-in min() function
print(sum([1, 2, 3]))  # Using the built-in sum() function
print(abs(-5))  # Using the built-in abs() function
print(round(3.14159, 2))  # Using the built-in round() function
print(sorted([3, 1, 2]))  # Using the built-in sorted() function
print(type(42))  # Using the built-in type() function