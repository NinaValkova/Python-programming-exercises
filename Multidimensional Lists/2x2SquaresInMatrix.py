def read_matrix(row, col):
    matrix = []
    
    for i in range(0, row):
        row = []
        line = input().split(' ')
        for j in range(0, col):
            element = line[j]
            row.append(element)
        matrix.append(row)    
    
    return matrix    
            
def find_matrix(matrix, row, col):
    counter = 0
    
    for i in range(0, row-1):
        for j in range(0, col-1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                counter+=1
    
    return counter            
     
    

line = input().split(' ')
row = int(line[0])
col = int(line[1])
matrix = read_matrix(row, col)
squares = find_matrix(matrix, row, col) 
print(squares)