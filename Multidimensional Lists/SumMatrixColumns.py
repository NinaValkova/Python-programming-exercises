from array import array

def read_matrix(rows, cols):
    my_array = array('i')
    
    number = 0
    for i in range(0, rows):
        line = input().split()
        for j in range(0, cols):
            element = int(line[j])
            my_array.append(element)
    
    return my_array        

def get_sum(rows, cols, matrix):
    sum_columns = array('i')
    sum = 0
    for i in range(0, cols):
        for j in range(0, rows):
            index = i + j*cols
            sum += matrix[index]
        sum_columns.append(sum)
        sum = 0
    return  sum_columns      

def print_sum(column_sum):
    size = len(column_sum)
    for i in range(0, size):
        print(column_sum[i])               

line = input().split(', ')
rows = int(line[0])
cols = int(line[1])

matrix = read_matrix(rows, cols)
column_sum = get_sum(rows, cols, matrix)
print_sum(column_sum)