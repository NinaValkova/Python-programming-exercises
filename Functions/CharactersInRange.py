character_1 = input()
character_2 = input()

start = ord(character_1)
end = ord(character_2)

for i in range(start + 1, end ,1):
    symbol = chr(i)
    print(symbol, end=' ')