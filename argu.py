def get_max(*num):
    if len(num)==0:
        return None
    max_num=num[0]
    for n in num:
        if n > max_num:
            max_num=n
    return max_num
print(get_max(2,6,4,88,29,99))
print(get_max('Bushra','Ariz','Mubina'))


def get_max(*num):
    if len(num) == 0:
        return None

    max_num = num[0]

    for n in num:
        if len(n) > len(max_num):
            max_num = n

    return max_num

print(get_max('Bushra', 'Ariz', 'Mubina'))
print(get_max('Apple', 'Watermelon', 'Kiwi'))
#
# LEGB rule: Local, Enclosing, Global, Built-in
x = 100  # Global

def outer():
    x = 50  # Enclosing

    def inner():
        x = 10  # Local
        print(x)

    inner()

outer()
