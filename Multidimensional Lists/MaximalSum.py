def read_matrix(row, col):
    matrix = []
    for i in range(0, row):
        line = input().split(' ')
        row = []
        for j in range(0, col):
            element = int(line[j])
            row.append(element)
        matrix.append(row)    
    
    return matrix        
    
def find_sum(matrix, row, col):
    max_sum =-1
    best_row = -1
    best_col = -1
    for i in range(0, row-2):
        for j in range(0, col-2):
            sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
            
            if max_sum < sum:
                best_row = i
                best_col = j
                max_sum = sum
    
    print(f'Sum = {max_sum}')     
    
    for i in range(best_row, best_row + 3):
         print(" ".join(str(matrix[i][j]) for j in range(best_col, best_col + 3)))             
            

line = input().split(' ')
row = int(line[0])
col = int(line[1])

matrix = read_matrix(row, col)
find_sum(matrix, row, col)
