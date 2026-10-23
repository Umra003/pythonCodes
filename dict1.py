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

# nested dictionaries:
d1={
    "info1":{  #d1 is main dict while info1 and info2 are nested dict in d1 each nested dict need a unique key
        'stud1':'umra',  #info1 and info2 are unique keys for nested dictionaries
        'age':22,
        'place':'sangli'
    },
    'info2':{
        'stud2':'mubina',
        'age':23,
        'place':'pune'
    }
}
print(d1) #prints all the key values in d1
for key,value in d1.items():   #this will print key value pairs of info1 and info separetly
    print(key, value)
for key in d1.keys():#prints info1 and info2
    print(key)
for value in d1.values():#prints values in info1 and info2
    print(value)
# for i in d1.pop('info1'): #this will return info1 n pop it from dictionary
#     print(i)
# for i in d1.popitem(): #this will return last dict i.e info2 n pop it from dictionary
#     print(i)
del d1['info1']
print(d1)#it will print info2 and info1 will be deleted from memory.

# d2={}
# d2.append({
#     'name':'bushra',
#     'age':23,
#     'place':'mumbai'
# }
# )
# print(d2) #causes error becoz dict dont have append method it have update method to add values


d2={} #creating empty dict and adding key values using the update method
d2.update({
    'name':'bushra',
    'age':23,
    'place':'mumbai'
}
)
print(d2)


d3=[] #here we created an empty list and inserted a dict key value pairs using append method.
d3.append({
    'name':'tapsira',
    'age':20,
    'place':'oman'
}
)
print(d3)


# Create an empty dictionary and perform the following tasks:
dict1={}
# 1. Add a student's name, age, city, and marks.
dict1.update({
    'name':"abc",
    'age':22,
    'city':'pune',
    'marks':90
})
# 2. Display the complete information.
print(dict1)
# 3. Display only the student's name and marks.
print(dict1['name'],dict1['marks'])
# 4. Change the student's marks to 92.
dict1['marks']=92
print(dict1)
# 5. Add the student's email address.
dict1['email']="abc@gmail.com"
print(dict1)
# 6. Remove the city information.
# dict1.remove['city'] it doent have remove method.
dict1.pop('city')
print(dict1)
# 7. Check whether the age information exists.
print('age' in dict1)
# 8. Display all remaining information.
print(dict1)
