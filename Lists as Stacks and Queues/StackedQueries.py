# Push sequence: 5, 3, 7
# main_stack: 5 → 5,3 → 5,3,7
# min_stack:  5 → 5,3 → 5,3,3
# Querying min_stack[-1] always gives current minimum.

# Every push/pop operation keeps the two stacks aligned.


from collections import deque

n = int(input())

main_stack = deque()
max_stack = deque()
min_stack = deque()

for i in range(0, n):
    line = input().split()
    command = int(line[0])
    
    if command == 1:
        number = int(line[1])
        main_stack.append(number)
        
        # True if the max_stack is empty - used to initialize the stack with the first element.
        if not max_stack:
            max_stack.append(number)
        else: 
            max_number = max_stack[-1]
            if max_number < number:
                max_stack.append(number)
            else:
               max_stack.append(max_number)     
                
        if not min_stack:
            min_stack.append(number)   
        else:
            min_number = min_stack[-1]
            if  number < min_number:
                min_stack.append(number)
            else:
               min_stack.append(min_number)    
                
    elif command == 2 and main_stack:
        main_stack.pop()
        max_stack.pop()
        min_stack.pop()
        
    # If the command is 3 and the max_stack is not empty    
    elif command == 3  and max_stack: 
        max_number = max_stack[-1]
        print(max_number)  
        
    elif command == 4 and min_stack:
        min_number = min_stack[-1]
        print(min_number)

numbers = []
size = len(main_stack)
for i in range(0, size):
    number = main_stack.pop()
    numbers.append(str(number))

output = ', '.join(numbers)
print(output)    
                
        
        
# from collections import deque

# n = int(input())  
# stack = deque()   

# for i in range(0, n):
#     query = input().split()
    
#     if query[0] == "1":        
#         number = int(query[1])
#         stack.append(number)
        
#     elif query[0] == "2":       
#         if stack:
#             stack.pop()
            
#     elif query[0] == "3":      
#         if stack:
#             print(max(stack))
            
#     elif query[0] == "4":       
#         if stack:
#             print(min(stack))

# print(", ".join(map(str, reversed(stack))))
        