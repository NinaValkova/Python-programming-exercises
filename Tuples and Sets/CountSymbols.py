line = input()

character_occurrences = {}
size = len(line)
for character in line:
    if character not in character_occurrences:
        character_occurrences[character] = 1
    else:
        character_occurrences[character] += 1

# character_occurrences = sorted(character_occurrences.items()) # returns a list of tuples (not a dictionary anymore).

# for character, occurrences in character_occurrences:
#     print(f'{character}: {occurrences} time/s')     

characters = list(character_occurrences.items())  
size = len(characters)
for i in range(0, size):
    for j in range(0, size - i- 1):
        # characters[0] → gets ('a', 2).
        # characters[j][0] → gets the first element of that tuple, i.e. the character ('a')
        if characters[j][0] > characters[j+1][0]:
            characters[j], characters[j+1] = characters[j+1], characters[j]

sorted_characters = dict(characters) 
for character, occurrences in sorted_characters.items():
    print(f'{character}: {occurrences} time/s')     
           
        