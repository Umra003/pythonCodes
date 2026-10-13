with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

    count=0
    for ch in content:
        if ch in 'aeiouAEIOU':
            count += 1  

    # count_of_aeiou=0
    # count_of_aeiou = content.lower().count('aeiou')
    # count_of_aeiou += content.lower().count('a')
    # count_of_aeiou += content.lower().count('e')
    # count_of_aeiou += content.lower().count('i')
    # count_of_aeiou += content.lower().count('o')
    # count_of_aeiou += content.lower().count('u')

     # Count occurrences of the characters 'a', 'e', 'i', 'o', 'u' in the file content
    print("Count of vowels in the file:", count)
