line = input()

words = line.split()

character_occurrences = {}

size = len(words)
for i in range(0, size):
    for character in words[i]:
        if character not in character_occurrences:
            character_occurrences[character] = 1
        else:
            character_occurrences[character] += 1

for key, value in character_occurrences.items():
    print(f'{key} -> {value}')              