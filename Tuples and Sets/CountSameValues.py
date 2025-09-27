# line = input()
# numbers = line.split()

# number_occurrences = dict()

# size = len(numbers)
# number = 0
# for i in range(0, size):
#     number = float(numbers[i])
#     if number not in  number_occurrences:
#         number_occurrences[number] = 1
#     else:    
#         number_occurrences[number] += 1 

# for number, occurrences in number_occurrences.items():
#      print(f'{number} - {occurrences} times' )    


line = input()
numbers = tuple(map(float, line.split()))

unique_numbers = set()

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.add(number)
        print(f'{number} - {numbers.count(number)} times')


     