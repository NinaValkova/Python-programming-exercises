from collections import deque

def print_input(line,start_index, end_index):
    for j in range(start_index ,end_index+1, 1):
        print(line[j], end='')
    print()
    
    
    
line = input()

stack = deque()

size = len(line)
for i in range(0, size, 1):
    if line[i] == '(':
        stack.append(i)
    elif line[i] == ')':
        start_index = stack.pop()  
        print_input(line,start_index, i)
         