n = int(input())
reservation_numbers = set()

for i in range(0, n):
    number = input()
    reservation_numbers.add(number)

line = input()
while(line != 'END'):
    if line in reservation_numbers:
        reservation_numbers.remove(line)
    line = input()

reservation_numbers = sorted(reservation_numbers)
size = len(reservation_numbers)    
print(size)
for number in reservation_numbers:
    print(number)