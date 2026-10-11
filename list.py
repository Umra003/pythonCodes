l1=[10,20,20,40,80,20,100]
print("List is:",l1)
# using list methods:
# 1. append() is used to add an element at the end of the list(only one element or object at a time) 
l1.append(120)
print("List after appending 120:",l1)
l1.append([34,78,67])
print("List after appending [34,78,67]:",l1) #[34,78,67] is added as a single element at the end of the list

#2.extend() is used to add multiple elements at the end of the list
l1.extend([140,160,180])
print("List after extending with [140,160,180]:",l1)

#3.insert() is used to add an element at a specific index in the list
l1.insert(4,88)
print("List after inserting 88 at index 4:",l1)

#4.remove() is used to remove the first occurrence of a specific element from the list
l1.remove([34,78,67]) #removes the first occurrence of [34,78,67] from the list
print("List after removing [34,78,67]:",l1)

#5.pop() is used to remove an element at a specific index from the list and return it. If no index is specified, it removes and returns the last element.
removed_element = l1.pop() #removes the element at end of the list and returns it
print("List after popping element at end:",l1)
print("Removed element:", removed_element)
removed_element = l1.pop(5) #removes the element at index 5 and returns it
print("List after popping element at index 5:",l1)
print("Removed element:", removed_element)

#6. clear() is used to remove all elements from the list
# l1.clear()
# print("List after clearing all elements:",l1)   
# print("Length of list after clearing:",len(l1)) #0

#7. index() is used to find the index of the first occurrence of a specific element in the list
index_of_88 = l1.index(88)
print("Index of 88:", index_of_88)

#8. count() is used to count the number of occurrences of a specific element in the list
count_of_20 = l1.count(20)
print("Count of 20:", count_of_20)

#9. sort() is used to sort the elements of the list in ascending order
l1.sort()
print("List after sorting in ascending order:",l1)

#10. reverse() is used to reverse the order of elements in the list
l1.reverse()        
print("List after reversing the order of elements:",l1)

#11. descending sort() is used to sort the elements of the list in descending order
l1.sort(reverse=True)   
print("List after sorting in descending order:",l1)

#12. copy() is used to create a shallow copy of the list
l2 = l1.copy()
print("Copied list l2:",l2)
l2.append(598)
print("List l2 after appending 598:",l2)
print("List l1 after appending 598 to l2:",l1)#no change in l1 as l2 is a copy of l1

#13. SLICING: slicing is used to create a new list that contains a portion of the original list
l3 = l1[2:5] #creates a new list l3 that contains elements from index 2 to 4 of l1
print("Sliced list l3 (from index 2 to 4):",l3)

l4 = l1[::2] #creates a new list l4 that contains every second element of l1
print("Sliced list l4 (every second element):",l4)

l5 = l1[::-1] #creates a new list l5 that contains the elements of l1 in reverse order
print("Sliced list l5 (elements in reverse order):",l5) 

l6=l1[:6]
print("Sliced list l6 (first 6 elements):",l6)

l7=l1[:8]
print("Sliced list l7 (elements upto to 7):",l7)
