lines = int(input())

letter =''
total_sum = 0

for i in range(0, lines, 1):
    letter = input()  
    total_sum += ord(letter)  # ord() If the argument is a one-character string, return the Unicode code point of that character

print(f'The sum equals: {total_sum}')    