n = int(input())

for i in range(0,n):
    line = input()
    size = len(line)
    for j in range(0, size, 1):
        if line[j] == ',' or line[j] == '.' or line[j] == '_':
            print(f'{line} is not pure!')
            break
    else:
        print(f'{line} is pure.')      