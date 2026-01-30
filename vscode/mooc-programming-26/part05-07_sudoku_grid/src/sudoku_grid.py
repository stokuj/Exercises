def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    
    my_list = []
    
    try:
        for i in range(3):
            for j in range(3):
                if sudoku[row_no+i][column_no+j] != 0:
                    if sudoku[row_no+i][column_no+j] in my_list:
                        return False
                    else:
                        my_list.append(sudoku[row_no+i][column_no+j])
                   
        return True
    except:
        print('Error: ')

def column_correct(sudoku: list, column_no: int) -> bool:
    
    my_list = []
    for i in range(len(sudoku)):
        
        if sudoku[i][column_no] != 0:
            if sudoku[i][column_no] in my_list:
                return False
            else:
                my_list.append(sudoku[i][column_no])
    
    return True

def row_correct(sudoku: list, row_no: int) -> bool:

    my_list = []
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] != 0:
            if sudoku[row_no][i] in my_list:

                return False
            else:
                my_list.append(sudoku[row_no][i])

    return True

def sudoku_grid_correct(sudoku: list)-> bool:
    flag = True
    for i in range(len(sudoku)):
        flag = column_correct(sudoku, i)
        if flag == False:
            return False
        
    for i in range(len(sudoku)):
        flag = row_correct(sudoku, i)
        if flag == False:
            return False
        
    for i in range(len(sudoku)//3):
        for j in range(len(sudoku)//3):
            flag = block_correct(sudoku, i*3, j*3)
            if flag == False:
                return False
            
    return flag


# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))
