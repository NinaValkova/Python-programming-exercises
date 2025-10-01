def read_matrix(n):
    matrix = []
    for i in range(0, n):
        row = []
        line = input().split()
        for j in range(0, n):
            element = int(line[j])
            row.append(element)
        matrix.append(row)
    
    return matrix        
            
def read_commands(n):
    commands = []
    line = input().split(' ')
    while line[0] != 'END':
        type_cmd = line[0]
        row = int(line[1])
        col = int(line[2])
        value = int(line[3])
        if col < 0 or row < 0 or col >= n or row >=n:
            commands.append('Invalid coordinates')
        else:
            commands.append((type_cmd, row, col, value))
        line = input().split(' ')
    
    return commands    
 
def fromat_matrix(matrix, commands):
    
    for cmd in commands:
        if cmd == 'Invalid coordinates':
            print(cmd)
        else:    
            type_cmd, row, col, value = cmd  
            if type_cmd == 'Add':
                matrix[row][col] += value
            elif type_cmd == 'Subtract':
                matrix[row][col] -= value

def print_matrix(matrix, n):
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=" ")
        print()    
                
    
n = int(input())

matrix = read_matrix(n)
commands = read_commands(n)
fromat_matrix(matrix, commands)
print_matrix(matrix, n)