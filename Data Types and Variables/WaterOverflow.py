lines = int(input())

capacity = 255
current = 0

for i in range(0, lines, 1):
    liters = int(input())

    if(current + liters > capacity):
        print('Insufficient capacity!')  
    else:
        current += liters    

print(current)