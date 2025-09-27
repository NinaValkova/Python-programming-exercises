n = int(input())

cars = set()
for i in range(0, n):
    line = input()
    line = line.split(", ")
    direction = line[0]
    carNumber = line[1]
    
    if direction == 'IN':
        cars.add(carNumber)
    elif direction == 'OUT':
        cars.remove(carNumber)   

if not cars:
  print('Parking Lot is Empty')  
else:
    for car in cars:
        print(car)         
    
    