from array import array

# can't really create a 2d array.array() because their elements
# are restricted to the types: characters, integers, and floating point numbers.
# Instead you could store your data in a regular one-dimensional array and access
# it through some helper functions.



def read_matrix():
    rows =0
    cols =0
    line = input().split(', ')
    rows = int(line[0])
    cols = int(line[1])
    
    my_array = array('i')
    for i in range(0, rows):
            elements = input().split(', ')
            for j in range(0, cols):
                element = int(elements[j])
                my_array.append(element)
    
    return rows, cols, my_array           
    
def get_sum(rows, cols, matrix):
    sum = 0
    for i in range(0, rows):
        for j in range(0, cols):
            index = i * cols + j
            sum += matrix[index]
    
    return sum        

def print_result(rows, cols, matrix, sum):
    print(sum)
    print_ln_form_of_list(rows, cols, matrix)
    
def print_ln_form_of_list(rows, cols, matrix):
    formatted_matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            index = i * cols + j
            row.append(matrix[index])
        formatted_matrix.append(row)    
                       
    print(formatted_matrix)                   

rows, cols, matrix = read_matrix()
sum = get_sum(rows, cols, matrix)
print_result(rows, cols, matrix, sum)