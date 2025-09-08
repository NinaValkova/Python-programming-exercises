n = int(input())

numbers = []

for i in range(0, n, 1):
    number = int(input())
    numbers.insert(i, number)

size = len(numbers)
for i in range(0, size, 1):
    if(numbers[i] == 88):
        print('Hello')
    elif(numbers[i] == 86):
        print('How are you?')
    elif(numbers[i] < 88):
        print('GREAT!') 
    else:
        print('Bye.')
