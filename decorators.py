# A decorator is a function that adds extra functionality to another function 
# without modifying its original code.


def decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")

    return wrapper


@decorator
def greet():
    print("Hello Umra!")


greet()