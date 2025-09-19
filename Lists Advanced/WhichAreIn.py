line_1 = input()
line_2 = input()

words_1 = line_1.split(", ")
words_2 = line_2.split(", ")

found_words = []

size = len(words_2)
for word in words_1:
    for i in range(0,size,1):
        #if words_2[i].find(word) != -1 and word not in found_words:
        if word in words_2[i] and word not in found_words: 
            found_words.append(word)

print(found_words)            