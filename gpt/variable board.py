def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    for row in range(size):
        print(" | ".join(board[row]))
        if row < size - 1:
            print("-" * (size * 2 - 1))

def check_winner(board, size):
    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == board[i][0] and board[i][0] != " " for j in range(size)):
            return board[i][0]
        if all(board[j][i] == board[0][i] and board[0][i] != " " for j in range(size)):
            return board[0][i]

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(size)):
        return board[0][0]
    if all(board[i][size - i - 1] == board[0][size - 1] and board[0][size - 1] != " " for i in range(size)):
        return board[0][size - 1]

    return None

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def play_game():
    size = int(input("Enter the size of the Tic Tac Toe board: "))
    board = create_board(size)
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row, col = map(int, input(f"Enter your move as row and column (0-{size-1}): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            continue

        if row < 0 or row >= size or col < 0 or col >= size or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board, size)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
