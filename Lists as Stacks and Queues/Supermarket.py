from collections import deque

def print_input(queue):
    size = len(queue)
    for i in range(0, size, 1):
        print(queue.popleft())

line = input()
queue = deque()
counter = 0
while line != 'End':
    counter +=1 
    if line == 'Paid':
        counter = 0
        print_input(queue)
    else:    
        queue.append(line) 
    
    
    line = input()

print(f"{counter} people remaining.")       