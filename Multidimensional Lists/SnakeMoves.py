line = input().split(' ')
rows = int(line[0])
cols = int(line[1])

word = input()
index = 0
length = len(word)
for i in range(0, rows, 1):
    current_word = ""
    for j in range(0, cols, 1):
        current_word += word[index % length] # picks the next character from the word
        index += 1 # move to the next character for the next iteration
    if i % 2 == 1:
        current_word = current_word[::-1]  # reverses the string to create the snake pattern
    
    print(current_word)      
           