line = input()

numbers = [int(x) for x in line.split()]

numbers = sorted(numbers)

print(numbers)