#A package is a folder containing related Python modules.
# Suppose you are creating a calculator project.
# You have many Python files:
# - add.py – addition
# - subtract.py – subtraction
# - multiply.py – multiplication
# Instead of keeping everything separately, you put these files inside one folder called calculator.
# This folder is called a package.
# __init__.py is a special file that we can put inside this folder to 
# initialize the package and control what happens when it is imported.


import calculator

from calculator.add import addition
from calculator.subtract import subtraction

print(addition(10, 5))
print(subtraction(10, 5))

#Another important use of __init__.py:
# from calculator.add import addition _instead of this we can use:
# from .add import addition
# from .subtract import subtraction(added in __init__.py)

#Now our main.py becomes:

from calculator import addition, subtraction

print(addition(10, 5))
print(subtraction(10, 5))
