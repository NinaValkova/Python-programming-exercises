def read_matrix(rows, cols):
    matrix = []
    
    for i in range(0, rows):
        line = input().split(', ')
        row = []
        for j in range(0, cols):
            element = int(line[j])
            row.append(element)
        matrix.append(row)  
    
    return matrix      
              
def find_sum_matrix_elements(matrix, rows, cols):
    max_sum = -1
    for i in range(0, rows-1):
        for j in range(0, cols-1):
            sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if max_sum < sum:
                element_right_top = matrix[i][j]
                element_left_top = matrix[i][j+1]
                element_right_buttom = matrix[i+1][j]
                element_left_buttom = matrix[i+1][j+1]
                max_sum = sum
    
    print(f'{element_right_top} {element_left_top}')
    print(f'{element_right_buttom} {element_left_buttom}')
    print(max_sum)            
            

line = input().split(', ')
rows = int(line[0])
cols = int(line[1])

matrix = read_matrix(rows, cols)
find_sum_matrix_elements(matrix, rows, cols)