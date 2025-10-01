def read_matrix(n):
    matrix = []
    
    
    for i in range(0, n):
        line = input().split(" ")
        row = []
        for j in range(0, n):
            element = int(line[j])
            row.append(element)
        matrix.append(row)
    
    return matrix     


def get_sum_pd(n, matrix):
    sum =0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                sum += matrix[i][j]
    
    return sum            
                
def get_sum_sd(n, matrix):
    sum =0
    for i in range(0, n):
        for j in range(0, n):
            if j == n-i-1:
                sum += matrix[i][j] 
    
    return sum                           
   

n = int(input())
matrix = read_matrix(n)
pd_sum = get_sum_pd(n, matrix)
sd_sum = get_sum_sd(n, matrix)
difference = abs(pd_sum - sd_sum)
print(difference)