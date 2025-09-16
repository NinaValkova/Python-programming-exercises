def readNumbers(size:int):
    numbers = []
    number = 0

    for i in range(0, size, 1):
        number = int(input())
        numbers.append(number)

    return numbers    


n = int(input())
numbers = readNumbers(n)

positive_numbers = []
count = 0

negative_numbers = []
sum = 0

for i in range(0, n, 1):
    if(numbers[i] > 0):
        positive_numbers.append(numbers[i])
        count+=1
    else:
        negative_numbers.append(numbers[i])
        sum += numbers[i]    

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {count}')
print(f'Sum of negatives:', sum)