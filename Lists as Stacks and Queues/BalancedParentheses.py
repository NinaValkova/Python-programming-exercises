from collections import deque
line = input()

stack = deque()
size = len(line)
balanced = True
for i in range(0, size, 1):
    if line[i] == '{':
        stack.append('{')
    elif line[i] == '[':
        stack.append('[')
    elif line[i] == '(':
        stack.append('(')  
     
    if line[i] == '}':
     # if not stack is necessary because of input } -stack is empty (no opening bracket yet).
     if not stack or stack.pop() != '{':
         balanced = False
         break
    elif line[i] == ']':
     if not stack or stack.pop() != '[':
         balanced = False
         break
    elif line[i] == ')':
     if not stack or stack.pop() != '(':
         balanced = False
         break

if balanced and not stack:
    print('YES')
else:
    print('NO')            
    
    
# from collections import deque

# line = input()
# stack = deque()
# # Keys are the closing parentheses: ), }, ].
# # Values are the corresponding opening parentheses: (, {, [.
# pairs = {')': '(', ']': '[', '}': '{'}  
# balanced = True

# for ch in line:
#     if ch in "([{":
#         stack.append(ch)
#     elif ch in ")]}":
#         # pairs[ch] gives the expected opening parenthesis that should match this closing one
#         if not stack or stack.pop() != pairs[ch]:
#             balanced = False
#             break

# if balanced and not stack:
#     print("YES")
# else:
#     print("NO")
    