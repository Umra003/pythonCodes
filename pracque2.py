with open ("demo.txt","r") as file:
    content=file.readlines()
    print("total lines in the file:",len(content))
    print("2nd line in the file is:",content[1])
    print("3rd line in the file is:",content[3])
