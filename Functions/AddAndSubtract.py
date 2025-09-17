def sum_numbers(number_1, number_2):
    return number_1 + number_2 
    
def subtract(sum, number_3):
    return sum-number_3

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

sum = sum_numbers(number_1, number_2) 
subtract = subtract(sum, number_3)

print(subtract)