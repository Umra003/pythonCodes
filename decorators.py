# A decorator is a function that adds extra functionality to another function 
# without modifying its original code.


def decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")

    return wrapper
@decorator    #shortcut for greet = decorator(greet)
def greet():
    print("Hello Umra!")
greet()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")

        func(*args, **kwargs)

        print("After execution")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Umra")