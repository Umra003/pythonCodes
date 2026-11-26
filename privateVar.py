# A private variable is a variable that is intended to be used only inside a class.

# In Python, we indicate a private variable by adding two underscores (__) before its name.
# class Student:
    # def __init__(self):
        # self.__marks = 90
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.show_balance()