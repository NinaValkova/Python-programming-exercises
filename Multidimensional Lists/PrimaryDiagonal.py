def read_matrix(rows):
    matrix = []
    for i in range(0, rows):
        row = []
        line = input().split()
        for j in range(0, rows):
            element = int(line[j])
            row.append(element)
        matrix.append(row)   
         
    return matrix        
 
def get_diagonal_sum(matrix, rows):
    sum = 0
    for i in range(0, rows):
         for j in range(0, rows):
             if i == j:
                 sum += matrix[i][j]
    return sum             
                

rows = int(input())
matrix = read_matrix(rows)
sum = get_diagonal_sum(matrix, rows)
print(sum)