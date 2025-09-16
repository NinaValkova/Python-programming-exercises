line = input()

numbers = [int(x) for x in line.split()]  # list comprehension

size = len(numbers)
for i in range(0, size, 1):
    negative = -1
    numbers[i] = numbers[i] * negative


print(numbers)
