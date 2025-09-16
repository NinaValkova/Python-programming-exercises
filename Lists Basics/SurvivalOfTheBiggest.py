line = input()
n = int(input())


numbers = [int(x) for x in line.split()]

size = len(numbers)

# Sort the list in-place - numbers.sort()
# Create a new sorted list. - sorted(numbers)
# sorted() function work for both strings and integers
sorted_numbers = sorted(numbers)

for i in range(0, n, 1):
    for j in range(0, size, 1):
        if sorted_numbers[i] in numbers:
            numbers.remove(sorted_numbers[i])


# size = len(numbers)
# for i in range(0,size-1,1):
#     print(numbers[i], end=', ')

# print(numbers[size-1])

# *numbers unpacks the list and passes each element (1, 2, 3, 4) as separate arguments to the print() function.
print(*numbers, sep=', ')