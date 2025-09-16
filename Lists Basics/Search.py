n = int(input())

word = input()

words = []
for i in range(0, n, 1):
    current_word = input()
    words.append(current_word)

certain_words=[]

for i in range(0, n, 1):
    if word in words[i]:
        certain_words.append(words[i])

print(words)
print(certain_words)