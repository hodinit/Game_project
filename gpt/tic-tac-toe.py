import numpy as np
import math

def create_board(size):
    return np.full((size, size), '-')

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, row, col):
    return 0 <= row < board.shape[0] and 0 <= col < board.shape[1] and board[row, col] == '-'

def make_move(board, row, col, player):
    board[row, col] = player

def check_winner(board, win_length):
    size = board.shape[0]

    # Check rows and columns
    for i in range(size):
        for j in range(size - win_length + 1):
            if all(board[i, j+k] == board[i, j] != '-' for k in range(win_length)) or \
               all(board[j+k, i] == board[j, i] != '-' for k in range(win_length)):
                return board[i, j]

    # Check diagonals
    for i in range(size - win_length + 1):
        for j in range(size - win_length + 1):
            if all(board[i+k, j+k] == board[i, j] != '-' for k in range(win_length)) or \
               all(board[i+k, j+win_length-1-k] == board[i, j] != '-' for k in range(win_length)):
                return board[i, j]

    return None

def is_draw(board):
    return '-' not in board

def evaluate(board, win_length, player):
    winner = check_winner(board, win_length)
    if winner == player:
        return 10
    elif winner is not None:
        return -10
    return 0

def minimax(board, depth, alpha, beta, maximizing, win_length, player, opponent):
    score = evaluate(board, win_length, player)
    if score == 10 or score == -10 or is_draw(board):
        return score

    if maximizing:
        max_eval = -math.inf
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i, j] == '-':
                    board[i, j] = player
                    eval = minimax(board, depth + 1, alpha, beta, False, win_length, player, opponent)
                    board[i, j] = '-'
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i, j] == '-':
                    board[i, j] = opponent
                    eval = minimax(board, depth + 1, alpha, beta, True, win_length, player, opponent)
                    board[i, j] = '-'
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board, win_length, player, opponent):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == '-':
                board[i, j] = player
                move_val = minimax(board, 0, -math.inf, math.inf, False, win_length, player, opponent)
                board[i, j] = '-'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def play_game():
    size = int(input("Enter board size (e.g., 3 for 3x3): "))
    win_length = int(input("Enter win length (e.g., 3 for 3 in a row): "))
    board = create_board(size)
    print_board(board)

    player = 'X'
    opponent = 'O'
    current_turn = 'X'

    while True:
        if current_turn == player:
            print("Your turn:")
            row, col = map(int, input("Enter row and column (0-indexed): ").split())
            if is_valid_move(board, row, col):
                make_move(board, row, col, player)
                print_board(board)
                if check_winner(board, win_length) == player:
                    print("You win!")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
                current_turn = opponent
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn:")
            row, col = find_best_move(board, win_length, opponent, player)
            make_move(board, row, col, opponent)
            print_board(board)
            if check_winner(board, win_length) == opponent:
                print("AI wins!")
                break
            elif is_draw(board):
                print("It's a draw!")
                break
            current_turn = player

if __name__ == "__main__":
    play_game()
