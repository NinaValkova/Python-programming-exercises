def print_numbers(numbers):
    size = len(numbers)
    
    for i in range(0, size-1, 1):
        print(numbers[i], end=', ')
    
    if size != 0:    
        print(numbers[size-1])
    else:
        print()    
        
line = input()

numbers = line.split(", ")

positive_numbers = [int(x) for x in numbers if int(x)>=0]
negative_numbers = [int(x) for x in numbers if int(x)<0]
even_numbers = [int(x) for x in numbers if int(x)%2 ==0]
odd_numbers = [int(x) for x in numbers if int(x)%2 !=0]

print(f'Positive: ', end='')
print_numbers(positive_numbers)

print(f'Negative: ', end='')
print_numbers(negative_numbers)

print(f'Even: ', end='')
print_numbers(even_numbers)

print(f'Odd: ', end='')
print_numbers(odd_numbers)