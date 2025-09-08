line = input()

size = len(line)

uppercase_letters = []
for i in range(0, size, 1):
    if line[i].isupper():
        uppercase_letters.append(i)

print(uppercase_letters)


