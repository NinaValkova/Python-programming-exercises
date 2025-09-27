n = int(input())

unique_elements = set()
for i in range(0, n):
    line = input().split()
    
    size = len(line)
    for j in range(0,size):
        unique_elements.add(line[j])

for element in unique_elements:
    print(element)
    