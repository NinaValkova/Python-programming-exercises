from collections import deque

quantity = int(input())

names = deque()

line = input()
while line != 'Start':
    names.append(line)
    
    line = input()

line = input()    
while line != 'End':
    
    parts = line.split()
    
    if parts[0] == 'refill':
        liters = int(parts[1]) 
        quantity += liters  
    else:
        liters = int(parts[0])
        name = names.popleft()
        if liters <= quantity:
            quantity -= liters
            print(f'{name} got water')
        else:    
            print(f'{name} must wait')  
        
    line = input()    
            
print(f'{quantity} liters left')            