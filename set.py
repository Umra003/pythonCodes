#sets in python are the collection of unordered and unindexed elements.
#They are mutable but cannot contain duplicate elements. 
#Sets are defined by placing the elements inside curly braces {} separated by commas or by using the built-in set() function.
s={}#will be treated as empty dictionary
s=set()#will be treated as empty set...set() is a built-in function that returns a new set object
s={1,2,3,4,5,6,8,2,6,7,8,9,10}#contains duplicate elements but will be treated as unique elements
print("Original set is: ",s)
#set methods
#1. add(): it is a method that adds an element to the set.
s.add(11)
print("Set after adding an element is: ",s)

#2. remove(): it is a method that removes the specified element from the set. If the element is not present, it raises a KeyError.
# s.remove(12) it will raise a KeyError because the element is not present in the set
s.remove(11) 
print("Set after removing an element is: ",s)

#3. pop(): it is a method that removes and returns first element from the set. If the set is empty, it raises a KeyError.
s.pop()
print("Set after popping an element is: ",s)

#4. discard(): it is a method that removes the specified element from the set. If the element is not present, it does nothing.
s.discard(12) #it will do nothing because the element is not present in the set
s.discard(11) #it will remove the element from the set
print("Set after discarding an element is: ",s) 
#difference between remove() and discard() is that remove() raises a KeyError if the element is not present in the set
#whereas discard() does nothing if the element is not present in the set

#5. clear(): it is a method that removes all the elements from the set.
# s.clear()

#6. union(): it is a method that returns a new set that contains all the elements from both sets.
s1={1,2,3,4,5}  
s2={4,5,6,7,8}
s3=s1.union(s2)
print("Union of sets is: ",s3)

#7. intersection(): it is a method that returns a new set that contains only the elements that are common to both sets.
s4=s1.intersection(s2)  
print("Intersection of sets is: ",s4)

#8. difference(): it is a method that returns a new set that contains only the elements that are present in the first set but not in the second set.
s5=s1.difference(s2)    #all the elements of s1 that are not present in s2 will be returned
print("Difference of sets is: ",s5)

#9. symmetric_difference(): it is a method that returns a new set that contains only the elements that are present in either of the sets but not in both.
s6=s1.symmetric_difference(s2)  #all the elements of s1 and s2 that are not present in both sets will be returned
print("Symmetric difference of sets is: ",s6)

#10. issubset(): it is a method that returns True if all the elements of the set are present in the specified set, otherwise it returns False.
s7={11,45,16} 
 #it will return False because not all the elements of s7 are present in s1 
print("Is s7 a subset of s1? ",s7.issubset(s1)) #it will return False because not all the elements of s7 are present in s1

#11. issuperset(): it is a method that returns True if all the elements of the specified set are present in the set, otherwise it returns False.
 #it will return False because not all the elements of s7 are present in s1
print("Is s1 a superset of s7? ",s1.issuperset(s7)) #it will return False because not all the elements of s7 are present in s1

#12. isdisjoint(): it is a method that returns True if the set has no elements in common with the specified set, otherwise it returns False.
s8={12,13,14}   
print("Is s8 disjoint from s1? ",s8.isdisjoint(s1)) #it will return True because s8 and s1 have no elements in common

#13. len(): it is a method that returns the number of elements in the set.
print("Length of the set is: ",len(s1)) #it will return the number of elements in the set s1    
