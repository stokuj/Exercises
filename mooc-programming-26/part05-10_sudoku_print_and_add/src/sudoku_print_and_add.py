def print_sudoku(sudoku: list):
    size = len(sudoku)
    for i in range(size):
        if i != 0 and i % 3 == 0:
            print('')
        for j in range(size):
            if j != 0 and j % 3 == 0:
                print(' ', end='')
            if sudoku[i][j] == 0:
                print('_', end=' ')
            else:
                print(sudoku[i][j],end=' ')

        print('')    
    
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    try:
        sudoku[row_no][column_no] = number
    except:
        print('Error:')


# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# print_sudoku(sudoku)
# add_number(sudoku, 0, 0, 2)
# add_number(sudoku, 1, 2, 7)
# add_number(sudoku, 5, 7, 3)
# print()
# print("Three numbers added:")
# print()
# print_sudoku(sudoku)