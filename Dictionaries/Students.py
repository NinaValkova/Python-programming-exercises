info = []

line = input()
while ":" in line:
    elements = line.split(':')
    info.append(elements)
    line = input()

course = line.replace('_', ' ')

size = len(info)
for i in range(0, size, 1):
    if course == info[i][2]:
        print(f'{info[i][0]} - {info[i][1]}')
        