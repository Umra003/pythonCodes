#string : sequence of characters.(immuatble, ordered and iterable) written using ' ', " ", """ """
num="0123456789"
print(num[0])#accesing by index value
print(num[-1])#accessing element from last.
print(num[1:5])#slicing(start:stop:step)
print(num[:5])
print(num[0:])
print(num[::2])
print(num[::-1])#reverse


game="   I love playing Badminton!  "
print(game.upper())
print(game.lower())
print(game.count('a'))
print(len(game))
print(game.split('-')) # converts it into list
print(game.strip()) #removes spaces
print(game.find('love'))
print(game.replace('love','like'))

game=["hello", "we", "are", "playing", "together!"] #this is a list which we need to convert it into string using join.
print(game)
print("".join(game))#returning string with no space
print(" ".join(game))##returning string with space
print("-".join(game))##returning string with hyphen


name='umra'#print each charcater or word using next line
for i in name:
    print(i)
