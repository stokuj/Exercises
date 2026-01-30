def row_correct(sudoku: list, row_no: int) -> bool:

    my_list = []
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] != 0:
            if sudoku[row_no][i] in my_list:

                return False
            else:
                my_list.append(sudoku[row_no][i])

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

# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))