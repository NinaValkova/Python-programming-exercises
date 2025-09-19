line = input()

version = list(map(int, line.split(".")))

carry = 1

size = len(version)
for i in range(size-1, -1, -1):
    version[i] += carry
    if version[i] == 10:
        version[i] = 0
        carry = 1
    else:
        carry = 0
        break    
        
version_str = '.'.join(map(str,version))
print(version_str)        