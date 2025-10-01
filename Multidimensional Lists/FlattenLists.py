line = input().split('|')

size = len(line)
result = []
for i in range(size-1, -1, -1):
    sub_line = line[i]
    clean_line = [int(x) for x in sub_line.split()]  
    length = len(clean_line)
    
    for j in range(0, length):
        result.append(clean_line[j])

size_result = len(result)        
for i in range(0, size_result):
    print(result[i], end = ' ')