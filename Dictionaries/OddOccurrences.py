line = input()

words = line.split()

words_occurrence = {}

size = len(words)
for i in range(0, size, 1):
    word = words[i].lower()
    
    if word not in words_occurrence:
        words_occurrence[word] = 0
    else:
        words_occurrence[word] += 1

for key, value in  words_occurrence.items():
    if value % 2 == 0:
        print(f'{key}', end=' ')       