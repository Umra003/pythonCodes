dict1={
    "name": "Umra",
    "subject": "Python",
    "roll_no": 125

}
print("Original dictionary is: ",dict1)

#dictionary is a collection of key-value pairs
#It is mutable, unordered and indexed(keys are unique and immutable but values can be duplicated and mutable)
#they are accessed by key values

#dictionary methods
# 1. updating existing key-value pairs
dict1["name"] = "Mubina"
dict1["roll_no"] = 126
print("Updated dictionary is: ",dict1)

#2. adding new key-value pairs
dict1["age"] = 20
print("Dictionary after adding new key-value pair is: ",dict1)

#3. deleting key-value pairs
del dict1["subject"] #del is keyword used to delete key-value pairs from dictionary
print("Dictionary after deleting key-value pair is: ",dict1)

#4. items(): it is a method that returns a view object that displays a list of a dictionary's "key-value" tuple pairs.
print("All key-value pairs in the dictionary are: ",dict1.items())

#5. keys(): it is a method that returns a view object that displays a list of all the "keys" in the dictionary.
print("All keys in the dictionary are: ",dict1.keys())

#6. values(): it is a method that returns a view object that displays a list of all the "values" in the dictionary.
print("All values in the dictionary are: ",dict1.values())  

#7. get(): it is a method that returns the value of the specified key.(the get() method returns None if the key does not exist)
print("Value of the key 'Name' is: ",dict1.get("Name")) #it will return None because the key is case sensitive
print("Value of the key 'name' is: ",dict1.get("name")) #it will return the value of the key 'name' if it exists

#8. pop(): it is a method that removes the specified key and returns the corresponding value.
print("Value of the key 'age' is: ",dict1.pop("age")) #it will remove the key 'age' and return its value

#9. popitem(): it is a method that removes the "last" inserted key-value pair from the dictionary and returns it as a tuple.
print("Last inserted key-value pair is: ",dict1.popitem()) #it will remove the last inserted key-value pair and return it as a tuple

#10. clear(): it is a method that removes all the key-value pairs from the dictionary.
# dict1.clear()