line = input().split(' ')
rows = int(line[0])
cols = int(line[1])

matrix = []
for i in range(0, rows):
    row = []
    line = input().split(' ')
    for j in range(0, cols):
        elements = line[j]
        row.append(elements)
    matrix.append(row)    
        
line = input().split(' ')
input_line = []
while line[0] != 'END':
    row0 = line[0]
    if len(line) != 5 or line[0] != 'swap':
        input_line.append('Invalid input!')
        line = input().split(' ') 
        continue
    row1 = int(line[1])
    col1 = int(line[2])
    row2 = int(line[3])
    col2 = int(line[4])
     
   
    if row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0 or row1 >= rows or col1 >= cols or row2 >= rows or col2 >= cols:
        input_line.append('Invalid input!')    
    else:      
        input_line.append((row1,col1,row2,col2))
         
    line = input().split(' ')  
       
 
for command in input_line:   
     
    if command == 'Invalid input!':
        print(command)
    else:
        row1, col1, row2, col2 = command
     
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
     
        for row in matrix:
           print(' '.join(map(str, row)))
     
     
     
          