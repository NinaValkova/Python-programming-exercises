line = input()

name_number = {}

while '-' in line:
    info = line.split('-')
    name = info[0]
    phone = info[1]
    name_number[name] = phone
    
    line = input()

n = int(line)
for i in range(0, n, 1):
    name = input()   
    
    if name in name_number:
        print(f'{name} -> {name_number[name]}')
    else:
        print(f'Contact {name} does not exist.')    