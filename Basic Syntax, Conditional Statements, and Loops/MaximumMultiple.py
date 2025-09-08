import math

divisor = int(input())
boundary = int(input())

max = -math.inf
for i in range(1, boundary+1):
    if(i%divisor == 0 and i > max):
        max = i

print(max)