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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    try:
        new_sudoku = [row.copy() for row in sudoku]
        new_sudoku[row_no][column_no] = number
    except:
        print('Error:')
    return new_sudoku

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

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)