def read_matrix(n):
    
    matrix = []
    for i in range(0, n):
        row = []
        line = input().split(", ")
        for j in range(0,n):
            element = int(line[j])
            row.append(element)
        matrix.append(row)    
    
    return matrix    
    
  
def print_solution(matrix, n): 
    
    primary_diagonal = []
    secondary_diagonal = []
    
    primary_diagonal_sum =0
    secondary_diagonal_sum =0
    for i in range(0, n):
        for j in range(0,n):
            if i == j:
                primary_diagonal_sum += matrix[i][j]
                primary_diagonal.append(matrix[i][j])
            
            if j == n-i-1:
                secondary_diagonal_sum += matrix[i][j]
                secondary_diagonal.append(matrix[i][j])
                
    size_pd = len(primary_diagonal)  
    size_sd  = len(secondary_diagonal)   
    
    print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
    print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
    
n = int(input())
matrix = read_matrix(n)
print_solution(matrix, n)