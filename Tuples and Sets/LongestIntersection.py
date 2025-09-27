n = int(input())

intrsection = []
length = 0
max_length = -1

for i in range(0, n):
    first_line, second_line = input().split('-')
    first_set = set()
    first_start, first_end = map(int, first_line.split(','))
    for i in range(first_start, first_end+1):
        first_set.add(i)
    
    second_set = set()
    second_start, second_end = map(int, second_line.split(','))
    for i in range(second_start, second_end+1):
        second_set.add(i)
    
    
    current_intersection = first_set & second_set
    length = len(current_intersection)
    if max_length < length:
        max_length = length
        # intrsection.clear()
        # for element in current_intersection:
        #     intrsection.append(element)
        intrsection = list(current_intersection)
        
print(f'Longest intersection is {intrsection} with length {max_length}')           
        