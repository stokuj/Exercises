def who_won(game_board: list) -> int:
    points1, points2 = 0, 0 
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):

            if game_board[i][j]   == 1:
                points1 += 1
            elif game_board[i][j] == 2:
                points2 += 1

    if points1 == points2:
        return 0
    elif points1 > points2:
        return 1
    else:
        return 2

#board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
#print(who_won(board))