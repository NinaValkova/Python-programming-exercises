line = input()

numbers = [float(x) for x in line.split()]
positive_numbers = []

for number in numbers:
    positive_number = abs(number)
    positive_numbers.append(positive_number)


print(positive_numbers)    