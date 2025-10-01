def read_matrix(n):
    matrix = []
    for i in range(0, n):
        line = input()
        row = []
        for j in range(0, n):
            row.append(line[j])
        matrix.append(row) 
    return matrix     

def is_element_in_matrix(n, matrix, symbol):
    row = -1
    cols = -1
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == symbol:
                print(f'({i}, {j})')
                return
    
    print(f'{symbol} does not occur in the matrix')    
                    

n = int(input())
matrix = read_matrix(n)
symbol = input()

is_element_in_matrix(n, matrix, symbol)
