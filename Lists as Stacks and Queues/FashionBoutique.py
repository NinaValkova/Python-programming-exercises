from collections import deque

line = input()
capacity = int(input())

clothes = line.split()

stack = deque()
sum = 0
size = len(clothes)
rack = 1
for i in range(0, size):
    cloth = int(clothes[i])
    
    sum += cloth
    if sum > capacity:
        sum = cloth
        rack +=1

print(rack)    