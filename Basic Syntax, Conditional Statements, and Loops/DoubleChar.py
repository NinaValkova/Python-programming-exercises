line = input()

while line != 'End':
    if(line != 'SoftUni'):
        size = len(line)
        for i in range(0, size):
            print(f'{line[i]}'*2, end='')

        print()    
    line = input()
   