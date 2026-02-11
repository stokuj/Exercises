def transpose(matrix: list):
    rows = len(matrix)
    cols = len(matrix[0])
    
    matrix2 = []
    for _ in range(cols):
        row = [0] * rows  
        matrix2.append(row)
    
    for i in range( len(matrix)):
        for j in range(len(matrix[i])):
            matrix2[j][i] = matrix[i][j]
    
    matrix[:] = matrix2
    
# list1 = [[1, 2, 3, 4], 
#          [5, 6, 7, 8]]

# print(transpose(list1))