def get_sum_even(number):
    sum = 0
    
    for digit in number:
        digit = int(digit) 
        
        if digit % 2 == 0:
            sum += digit
    
    return sum
 
def get_sum_odd(number):
    sum = 0
    
    for digit in number:
        digit = int(digit) 
        
        if digit % 2 == 1:
            sum += digit
    
    return sum             
            

number = input()

sum_even = get_sum_even(number)
sum_odd = get_sum_odd(number)

print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')