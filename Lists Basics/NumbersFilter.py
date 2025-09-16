n  = int(input())
numbers = []

for i in range(0,n,1):
    number = int(input())
    numbers.append(number)

command = input()

filtered = []

match(command):
    case 'even':
        for number in numbers:
            if number % 2 == 0:
                filtered.append(number)
    case 'odd':
        for number in numbers:
            if number % 2 == 1:
                filtered.append(number)
    case 'negative':
        for number in numbers:
            if number < 0:
                filtered.append(number) 
    case 'positive':
        for number in numbers:
            if number >= 0:
                filtered.append(number)

print(filtered)
