# Trying start at pump 0:
#   Pump 0: +1 petrol, need 5 → tank = -4
#   Failed at pump 0 (tank < 0).

# Trying start at pump 1:
#   Pump 1: +10 petrol, need 3 → tank = 7
#   Pump 2: +3 petrol, need 4 → tank = 6
#   Pump 0: +1 petrol, need 5 → tank = 2
# Success! Start index is 1

def make_circle(amount_petrol, distance, size):
    
    for i in range(0, size, 1):
        start_index =  i
        completed = True
        tank =0
        for j in range(0, size, 1):
            index = (start_index + j) % size # ensures circular indexing (when reaching the end, wrap back to 0)
            fuel = amount_petrol[index] - distance[index]
            tank += fuel
        
            if tank < 0:
                completed = False
                break
    
        if completed:
            return start_index        
        

n = int(input())
amount_petrol = []
distance = []
for i in range(0, n, 1):
    line = input().split()
    amount_petrol.append(int(line[0]))
    distance.append(int(line[1]))
    
start = make_circle(amount_petrol, distance, n)
print(start)