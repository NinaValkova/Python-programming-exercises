from collections import deque

line = input()

stack = deque()
for chr in line:
    stack.append(chr)

size = len(line)
for i in range(0, size, 1):
    print(stack.pop(), end = '')    