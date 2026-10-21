#file IO operations:
#read, write, append, delete, rename, copy, move,seek,tell etc.
import os
print(os.getcwd())

#writing to a file:
with open("myfile.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("This file is created for demonstration purposes.\n")
    f.write("We are learning about file I/O operations in Python.\n")

#reading from a file:
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)

#appending to a file:
with open("myfile.txt", "a") as f:
    f.write("This line is appended to the file.\n")#though its appended but we need to use write mode to append data to a file.
#now read again to see the appended content:
with open("myfile.txt", "r") as f:
    c=f.read()
    print(c)


#specific read() operations read(), readline(), readlines():
# read(): reads the entire file
# readline(): reads one line
# readlines(): reads all lines as list
with open("myfile.txt", "r") as file:
    print(file.readline())#prints 1st line
    print(file.readline())#prints 2nd line

with open("myfile.txt") as f:
    print(f.readlines()) #in the form of list

#printing a particular line (use readlines()):
with open("myfile.txt") as f:
    c=f.readlines()
    print(c[2])


# The tell() method returns the current position of the file pointer.
with open("myfile.txt") as f:
    print(f.tell())
    c=f.readlines()
    print(c[2])
    print(f.tell())

# The seek() method moves the file pointer to a specified position.
with open("myfile.txt")as file:
    print(file.read(3))#reads 3 character from start
    print(file.tell())

    file.seek(1)

    print(file.read(2))
    print(file.tell())