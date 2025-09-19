line = input()
factor = int(input())

employees = line.split()

# map() returns an iterator, so list() casts it to a list.
happiness = lambda x: int(x)*factor
employees_happiness = list(map(happiness,employees))

# lambda_func returns True or False depending on whether the employee’s happiness is greater than or equal to the average happiness.
lambda_func = lambda x: x >= sum(employees_happiness)/len(employees_happiness)
employees_filtered = list(filter(lambda_func, employees_happiness))

size = len(employees)
average = len(employees_filtered)

if average >= size/2:
    print(f'Score: {average}/{size}. Employees are happy!')
else:
    print(f'Score: {average}/{size}. Employees are not happy!')
        