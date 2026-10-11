num=(12,34,56,78,90)
print("Tuple:",num)
# tuples are immutable, so we cannot change the elements of a tuple after it is created.
#  However, we can perform various operations on tuples.
print("Length of Tuple:",len(num))
print("Element at index 2:",num[2])
# num.append(100) 
# num[1]=45  # This will raise a TypeError since tuples are immutable


#methods of tuple

#1. count() is used to count the number of occurrences of a specific element in the tuple
count_of_34 = num.count(34)     
print("Count of 34:", count_of_34)

#2. index() is used to find the index of the first occurrence of a specific element in the tuple
index_of_78 = num.index(78)
print("Index of 78:", index_of_78)

#3. concatenation of tuples
num2 = (100,200,300)
num3 = num + num2
print("Concatenated Tuple:", num3)  

#4. repetition of tuples
num4 = num * 2  
print("Repeated Tuple:", num4)

#5. slicing of tuples(same as list slicing)
sliced_tuple = num[1:4] 
print("Sliced Tuple (index 1 to 3):", sliced_tuple)

sliced_tuple2 = num[::2]
print("Sliced Tuple (every second element):", sliced_tuple2)
