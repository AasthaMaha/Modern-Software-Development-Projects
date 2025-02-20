def print_board(board):
    """Displays the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the player has won the game."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def get_valid_move(board,player):
    """Will ask the player for a move and validate it."""
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and col (0-2): ").split())
            if row not in range(3) or col not in range(3):
                print("Out of range! Enter values between 0 and 2.")
            elif board[row][col] != " ":
                print("Spot already taken. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Enter two numbers separated by a space.")

        """Makes sure that players can't enter invalid values.'"""
        """Added messages to help  guide and understand what the players should enter.'"""

def tic_tac_toe():
    """Main function of the game. It will run the Tic-Tac-Toe game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_tokens = ["X", "O"]

    print("Tic-Tac-Toe Game")
    print_board(board)

    for turn in range(9):
        current_player = player_tokens[turn % 2]
        row, col = get_valid_move(board,current_player)

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        if is_full(board):
            print("It's a Draw!")
            return

    print("It's a Draw!")


tic_tac_toe()
