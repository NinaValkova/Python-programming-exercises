line = input()
numbers = line.split(', ')

size = len(numbers)

indices = []
for i in range(0, size, 1):
    number = int(numbers[i])
    if number % 2 == 0:
        indices.append(i)
        
print(indices)        
        