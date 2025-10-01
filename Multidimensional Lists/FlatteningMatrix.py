def  read_matrix(row):
    matrix = []
    for i in range(0, row):
        line = input().split(', ')
        size = len(line)
        for i in range(0, size):
            element = int(line[i])
            matrix.append(element)  
    print(matrix)          

row = int(input())
matrix = read_matrix(row)