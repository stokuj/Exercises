def column_correct(sudoku: list, column_no: int) -> bool:
    
    my_list = []
    for i in range(len(sudoku)):
        
        if sudoku[i][column_no] != 0:
            if sudoku[i][column_no] in my_list:
                return False
            else:
                my_list.append(sudoku[i][column_no])
    
    return True

# sudoku = [
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

# print(column_correct(sudoku, 0))
# print(column_correct(sudoku, 1))
