words = ['sand', 'water', 'fish', 'sun']

line = input()
line = line.lower()

count = 0
for word in words:
    count += line.count(word)

print(count)
