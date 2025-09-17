line = input()

numbers =[int(x) for x in line.split()]

lambda_func = lambda x : x % 2 == 0 

even_numbers = list(filter(lambda_func, numbers))

print(even_numbers)