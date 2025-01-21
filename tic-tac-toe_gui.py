import tkinter as tk
from tkinter import messagebox
import numpy as np
import math

def create_board(size):
    return np.full((size, size), '-')

def is_valid_move(board, row, col):
    return 0 <= row < board.shape[0] and 0 <= col < board.shape[1] and board[row, col] == '-'

def make_move(board, row, col, player):
    board[row, col] = player

def check_winner(board, win_length):
    size = board.shape[0]

    for i in range(size):
        for j in range(size - win_length + 1):
            if all(board[i, j+k] == board[i, j] != '-' for k in range(win_length)) or \
               all(board[j+k, i] == board[j, i] != '-' for k in range(win_length)):
                return board[i, j]

    for i in range(size - win_length + 1):
        for j in range(size - win_length + 1):
            if all(board[i+k, j+k] == board[i, j] != '-' for k in range(win_length)) or \
               all(board[i+k, j+win_length-1-k] == board[i, j] != '-' for k in range(win_length)):
                return board[i, j]

    return None

def is_draw(board):
    return '-' not in board

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

def minimax(board, depth, alpha, beta, maximizing, win_length, player, opponent):
    winner = check_winner(board, win_length)
    if winner == player:
        return 10
    elif winner == opponent:
        return -10
    elif is_draw(board):
        return 0

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

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.size = 3
        self.win_length = 3
        self.board = create_board(self.size)
        self.buttons = []
        self.player = 'X'
        self.opponent = 'O'
        self.current_turn = 'X'

        self.create_widgets()

    def create_widgets(self):
        for i in range(self.size):
            row_buttons = []
            for j in range(self.size):
                button = tk.Button(self.root, text='', font=('Arial', 24), width=4, height=2,
                                   command=lambda r=i, c=j: self.on_button_click(r, c))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, row, col):
        if self.current_turn == self.player and is_valid_move(self.board, row, col):
            self.make_move(row, col, self.player)
            if self.check_game_over():
                return
            self.current_turn = self.opponent
            self.root.after(500, self.ai_move)

    def ai_move(self):
        row, col = find_best_move(self.board, self.win_length, self.opponent, self.player)
        self.make_move(row, col, self.opponent)
        if not self.check_game_over():
            self.current_turn = self.player

    def make_move(self, row, col, player):
        self.board[row, col] = player
        self.buttons[row][col].config(text=player, state=tk.DISABLED)

    def check_game_over(self):
        winner = check_winner(self.board, self.win_length)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.reset_game()
            return True
        elif is_draw(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.board = create_board(self.size)
        self.current_turn = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
