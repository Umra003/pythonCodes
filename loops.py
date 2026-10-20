# looping statements in python are for, while 

# for loop:Used when you want to iterate over a sequence or repeat something a known number of times.
l1=[12,34,1.79,55] #using it to iterate list, tuple and string
for i in l1:
    print("List:",i)
l2=(22,"Umra",22.4)
for j in l2:
    print("Tuple:",j)
l3="Umra"
for i in l3:
    print("String:",i)

# for loop with range() function:
# range() used to iterate within specific range, includes start and stop but the stop value is always excluded!
# have 3 ways: range(start,stop,end), range(stop),range(start,stop,step)
for i in range(5):
    print("range with end:",i)#prints 0-4
for i in range(3,7):
    print(i)#prints from 3-6
    
for i in range(2,21,2):#step:Amount to increase or decrease each time
    print("range with start,stop and end:",i)

for i in range(10,2,-2):
    print("backwards:",i)

#while loop:used to repeat a block of code as long as a condition is True.
i = 2

while i <= 10:
    print("using while loop:",i)
    i += 2


i = 5
while i >= 1:
    print(i)
    i -= 1

word = "Python"
i = 0
while i < len(word):
    print(word[i])
    i += 1