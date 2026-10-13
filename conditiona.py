#using if-else statement
num=int(input("Enter a number: "))
if num>0:
    print("Using simple if-else statement")
    print("The number is positive")
else:
    print("Using simple if-else statement")
    print("The number is negative")

#using if-elif-else statement
num=int(input("Enter a number: "))
if num>0:
    print("Using if-elif-else statement")
    print("The number is positive")
elif num<0:
    print("Using if-elif-else statement")
    print("The number is negative")
else:
    print("Using if-elif-else statement")
    print("The number is zero")

#using nested if-else statement
num=int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("using nested if-else statement")
        print("The number is positive and even")
    else:
        print("using nested if-else statement")
        print("The number is positive and odd")
else:
    print("using nested if-else statement")
    print("The number is not positive")

#using conditional expression
num=int(input("Enter a number: "))
result = "positive" if num > 0 else "not positive" #shorthand for if-else statement
print("Using conditional expression")
print("The number is", result)

#using match-case statement(switch case statement), used when there are multiple conditions to check of fixed values
num=int(input("Enter a number: "))
match num:#macth is keyword and num is the variable to be checked
    case 0:
        print("Using match-case statement")
        print("The number is zero")
    case _ if num > 0:
        print("Using match-case statement")
        print("The number is positive")
    case _ if num < 0:
        print("Using match-case statement")
        print("The number is negative")

#another example of match-case statement
day=int(input("Enter a number between 1 and 7: "))  
match day:
    case 1:
        print("Using match-case statement")
        print("The day is Monday")
    case 2:
        print("Using match-case statement")
        print("The day is Tuesday")
    case 3:
        print("Using match-case statement")
        print("The day is Wednesday")
    case 4:
        print("Using match-case statement")
        print("The day is Thursday")
    case 5:
        print("Using match-case statement")
        print("The day is Friday")
    case 6:
        print("Using match-case statement")
        print("The day is Saturday")
    case 7:
        print("Using match-case statement")
        print("The day is Sunday")
    case _:
        print("Using match-case statement")
        print("Invalid day")