#reusable block of code that performs a particular task.
# def is a Python keyword used to define a function.
def my_function():#Defining: Creating the function using def.
    #parameters: Variables that can be passed to the function to customize its behavior. In this case, there are no parameters.
    # The code inside this function will be executed when the function is called.
    print("Hello from my_function!")

# Call the function: Executing the function by writing its name followed by parentheses ().
my_function()#arguments: Values passed to the function when calling it. In this case, there are no arguments.
my_function()  # Calling the function again to demonstrate reusability.


# Types of functions in Python:
# 1.no parameter and no return value:
def greet():
    print("Hello, welcome to the program!")
greet()  # Calling the function to execute its code.

# 2. no parameter but return value:
def get_greeting():
    return "Hello, welcome to the program!"

greeting = get_greeting()
print(greeting)

#3. parameter but no return value:
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program!")

greet_user("Umra")  # Calling the function with an argument.

#4. parameter and return value:
def add(a, b):
    return a + b

print(add(5, 3))

# Different ways to pass arguments: postional and keyword arguments.
# Positional arguments: The order of the arguments matters.
def greet(name, age):
    print(f"hello {name}, your age is {age}.")
greet("Mubina", 21)# name should be first and age should be second.
# Keyword arguments: The order of the arguments does not matter.
def greet(name, age):
    print(f"Hello {name}, your age is {age}.")
greet(age=22, name="Bushra")  # Using keyword arguments to specify the values.

# Default arguments: You can provide default values for function parameters. If the caller does not provide a value for that parameter, the default value will be used.
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Ayesha")



# *args and ** kwargs: Used to pass a variable number of arguments to a function.
# *args: Allows you to pass a variable number of positional arguments to a function.
def get_max(*numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for n in numbers:
        if n > max_num:
            max_num = n

    return max_num

print(get_max(2, 6, 4, 88, 29, 99))#returns in the form of tuple.
print(get_max("mubina", "ariz", "bushra"))  #returns in the form of tuple.

# **kwargs: Allows you to pass a variable number of keyword arguments to a function.
def print_key_value_pairs(**kwargs):#used when number of keyword arguments is unknown.
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_value_pairs(name="Mubbo", age=25, city="New York") #returns in the form of dictionary.
