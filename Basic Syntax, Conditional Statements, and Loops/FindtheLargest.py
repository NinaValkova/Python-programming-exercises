number = input()

digit_count = {}

for digit in number:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1

largest_number = ''
for d in sorted(digit_count.keys(), reverse=True):
    largest_number += d * digit_count[d]  

print(largest_number)        