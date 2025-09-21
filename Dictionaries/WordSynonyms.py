n = int(input())

word_synonym = {}
for i in range(0, n, 1):
    word = input()
    synonym = input()
    
    if word in word_synonym:
        word_synonym[word].append(synonym)
    else:
        word_synonym[word] = [synonym]

for word, synonym in word_synonym.items():
    print(f"{word} - {', '.join(synonym)}")    