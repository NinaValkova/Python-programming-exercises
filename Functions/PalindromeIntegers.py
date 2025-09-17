line = input()

numbers = [int(x) for x in line.split(', ')]

size = len(numbers)

for i in range(0, size, 1):
    number_to_str = str(numbers[i])
    
    reverse_number = number_to_str[::-1]   
    if(number_to_str == reverse_number):
        print('True')
    else:
        print('False')    