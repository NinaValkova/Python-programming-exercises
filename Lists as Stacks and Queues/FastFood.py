from collections import deque

quantity = int(input())

line = input()
orders = line.split()

queue = deque()

max_order = -1
size = len(orders)
for i in range(0, size):
    order = int(orders[i])
    queue.append(order)
    
    if(max_order < order):
        max_order = order
     
print(max_order)

for i in range(0, size):
    current_order = queue[0]
    if quantity >= 0 and quantity >= current_order:
        quantity-= current_order
        queue.popleft()
    else: 
        break    

if not queue:
    print('Orders complete')
else:
    size = len(queue)
    print('Orders left:', end=' ')  
    for i in range(0, size):
        current_order = queue.popleft()  
        print(current_order, end = ' ')   