line = input()

numbers = [float(x) for x in line.split()]

size = len(numbers)
for i in range(0,size):
    numbers[i] = round(numbers[i])
    
print(numbers)    