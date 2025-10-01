def read_matrix(rows):
    matrix = []
    for i in range(0, rows):
        row = input().split(', ')
        size = len(row)
        
        numbers = []
        for i in range(0, size):
            element = int(row[i])
            numbers.append(element)
            
        matrix.append(numbers)
    
    return matrix    

def print_even(rows, matrix):
    
    matrix_even = []
    for i in range(0, rows):
        cols = len(matrix[i])
        row_matrix_even = []
        for j in range(0, cols):
            if matrix[i][j] % 2 ==0:
                 row_matrix_even.append(matrix[i][j])
        matrix_even.append(row_matrix_even)         
    
    print(matrix_even)              

rows = int(input())
matrix = read_matrix(rows)
print_even(rows, matrix)
