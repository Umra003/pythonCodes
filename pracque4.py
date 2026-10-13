with open ("demo.txt", "r") as file:
    word=file.read()
    words=word.split()
    print("Total words in the file:",len(words))
    print("Unique words in the file:",len(set(words)))