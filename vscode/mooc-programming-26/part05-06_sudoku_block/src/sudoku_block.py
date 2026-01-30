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

# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))
