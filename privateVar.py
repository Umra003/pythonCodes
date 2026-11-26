# A private variable is a variable that is intended to be used only inside a class.

# In Python, we indicate a private variable by adding two underscores (__) before its name.
# class Student:
    # def __init__(self):
        # self.__marks = 90
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance #__balance is a private variable.

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.show_balance()
# if you try to access the private variable directly, it will raise an AttributeError.
# class Student:

#     def __init__(self):
#         self.name = "Umra"          # Public
#         self._age = 22              # Protected convention
#         self.__marks = 90           # Private
# A getter is a method used to access or retrieve the value of a private variable.
# A setter is a method used to modify or update the value of a private variable.
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, new_balance):

        if new_balance >= 0:
            self.__balance = new_balance
            print("Balance updated successfully")

        else:
            print("Invalid balance! Cannot be negative.")


# Creating object
account = BankAccount(5000)

# Accessing private variable using getter
print("Current Balance:", account.get_balance())

# Updating private variable using setter
account.set_balance(8000)

# Accessing updated balance
print("Updated Balance:", account.get_balance())

# Trying invalid balance
account.set_balance(-2000)