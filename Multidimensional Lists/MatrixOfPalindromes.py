def print_matrix(matrix, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            print(matrix[i][j] , end = ' ')
        print()    

def generate_matrix(rows, cols):
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            output = f'{chr(97+i)}{chr(97+i+j)}{chr(97+i)}'
            row.append(output)
        matrix.append(row)   
    
    print_matrix(matrix, rows, cols)    

line = input().split(' ')
rows = int(line[0])
cols = int(line[1])

generate_matrix(rows, cols)