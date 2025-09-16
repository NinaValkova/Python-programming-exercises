line = input()
beggars = int(input())

numbers = [int(x) for x in line.split(',')]

sum = [0]*beggars

size=len(numbers)

for i in range(0,beggars,1):
    for j in range(i, size, beggars):
        sum[i]+=numbers[j]

print(sum)