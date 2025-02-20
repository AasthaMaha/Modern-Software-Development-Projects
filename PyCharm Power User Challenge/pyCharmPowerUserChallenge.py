def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board in a formatted manner.

    Args:
        board (list of list of str): A 2D list representing the Tic-Tac-Toe board.
                                     Each cell contains "X", "O", or a blank space.
                                     
    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """
    Checks if the given player has won the Tic-Tac-Toe game.

    A player wins if they have three of their tokens in a row either horizontally, 
    vertically, or diagonally on the board.

    Args:
        board (list of list of str): The 2D list representing the board.
                                     Each cell contains "X", "O", or a blank space.
        player (str): The token of the current player ("X" or "O").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    """
    Checks if the Tic-Tac-Toe board is full, meaning there are no empty spaces left.

    Args:
        board (list of list of str): A 2D list representing the Tic-Tac-Toe board.
                                     Each cell contains "X", "O", or a blank space.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board, player):
    """
    Prompts the player to enter a valid move and checks its validity.

    This function ensures that the player enters a move within the valid range (0-2)
    for both row and column, and that the selected cell is not already occupied.

    Args:
        board (list of list of str): A 2D list representing the Tic-Tac-Toe board.
                                     Each cell contains "X", "O", or a blank space.
        player (str): The token of the current player ("X" or "O").

    Returns:
        tuple: A tuple (row, col) indicating the valid move chosen by the player.
    """
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


def tic_tac_toe():
    """
    Main function of the Tic-Tac-Toe game. It initializes the game board and 
    runs the game loop where two players take turns making moves. The game 
    continues until there is a winner or the board is full, indicating a draw.

    Gameplay flow:
    1. Players take turns making a move by entering row and column indices.
    2. Each move is validated to ensure it is within range and not on an occupied cell.
    3. The board is updated after every valid move and printed to the console.
    4. The game checks for a winner or if the board is full after each turn.
    5. The game ends either with a winner or in a draw.

    Args:
        None

    Returns:
        None
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_tokens = ["X", "O"]

    print("Tic-Tac-Toe Game")
    print_board(board)

    for turn in range(9):
        current_player = player_tokens[turn % 2]
        row, col = get_valid_move(board, current_player)

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
