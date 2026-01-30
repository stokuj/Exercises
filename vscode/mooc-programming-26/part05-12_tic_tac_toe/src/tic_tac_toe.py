def play_turn(game_board: list, x: int, y: int, piece: str):
    if y < 0 or y >= len(game_board) or x < 0 or x >= len(game_board[0]):
        return False
    
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False
    
    
# game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
# print(play_turn(game_board, 2, 0, "X"))
# print(game_board)[['O', '', 'X'], ['X', '', 'O'], ['O', 'O', '']], 3, 0, X