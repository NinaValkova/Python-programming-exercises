line = input()
characters  = line.split(', ')
ascii_code = []

size = len(characters)
for i in range(0, size):
    ascii_code.append(ord(characters[i]))
    

character_ascii = {character:ascii for character, ascii in zip(characters, ascii_code)}

print(character_ascii)