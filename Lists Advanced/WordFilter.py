line = input()

words = line.split()

even_words = []

for word in words:
    size = len(word)
    if size % 2 == 0:
        even_words.append(word)

for word in even_words:
    print(word)        