def print_board(board):
    for r in board:
        print(" | ".join(r))
        print("-" * 5)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(c != " " for r in board for c in r)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    players(board)
    for t in range(9):
        pl = players[t % 2]
        while 1:
            try:
                row, col = map(int, input(f"P {pl}, row col (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = pl
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        players(board)
        if check_winner(board, pl):
            print(f"P {pl} wins!")
            return
        if is_full(board):
            print("Draw!")
            return
    print("Draw!")


tic_tac_toe()