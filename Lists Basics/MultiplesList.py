factor = int(input())
count = int(input())

numbers = []

number = 0
for i in range(1, count+1, 1):
    numbers.append(i*factor)

print(numbers)    