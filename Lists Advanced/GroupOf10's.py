# read input
line = input()

numbers = [int(x) for x in line.split(', ')]

max_value = max(numbers)

if max_value % 10 == 0:
    max_row = max_value // 10
else:
    max_row = (max_value // 10) +1   
    
groups = [[] for _ in range(max_row)]

# full matrix
size = len(numbers)
boundary = 10
prev_boundary = 0
for i in range(0, max_row, 1):
    for j in range(0, size, 1):
        if(numbers[j] <= boundary and numbers[j] > prev_boundary):
            groups[i].append(numbers[j])
    
    prev_boundary = boundary    
    boundary += 10

#print matrix
for i in range(len(groups)):
    print(f"Group of {i+1}0's: {groups[i]}")


#Using filter - second solution
# line = input()
# numbers = [int(x) for x in line.split(', ')]

# boundary = 10
# while numbers:
#     lambda_func = lambda x: x <= boundary
#     current_group = list(filter(lambda_func, numbers))
#     print(f"Group of {boundary}'s: {current_group}")
#     # remove processed numbers
#     numbers = [x for x in numbers if x > boundary]
#     boundary += 10        