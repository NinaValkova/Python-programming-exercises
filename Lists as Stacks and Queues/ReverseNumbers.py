from collections import deque
line = input()

numbers = line.split()

stack = deque(numbers)

size = len(numbers)
for i in range(0,size):
    number = stack.pop()
    print(number, end = ' ')