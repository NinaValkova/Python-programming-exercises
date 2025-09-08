word = input()

reversed_word = ''

size = len(word)
for i in range(size-1, -1, -1):
    reversed_word += word[i]

print(reversed_word)