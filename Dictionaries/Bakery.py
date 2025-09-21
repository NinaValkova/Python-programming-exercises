line = input()

elements = line.split()

table = {}

size = len(elements)
for i in range(0, size, 2):
    key = elements[i]
    value = int(elements[i+1])
    
    table[key] = value
    
print(table)    