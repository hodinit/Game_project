import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root, size):
        self.root = root
        self.size = size  # Board size (e.g., 3 for 3x3)
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(None)
            self.board.append(row)

        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []

        for row in range(self.size):
            button_row = []
            for col in range(self.size):
                button = tk.Button(
                    self.root,
                    height=5,
                    width=10,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def on_click(self, row, col):
        if self.board[row][col] is None and self.current_player == "X":  # Human's turn
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.destroy()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.destroy()
            else:
                self.current_player = "O"
                self.ai_move()

    def ai_move(self):
        best_score = -math.inf
        best_move = None

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    self.board[row][col] = "O"
                    score = self.minimax(0, False, -math.inf, math.inf)
                    self.board[row][col] = None
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", "AI wins!")
                self.root.destroy()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.destroy()
            else:
                self.current_player = "X"

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_winner_state("O"):
            return 10 - depth
        elif self.check_winner_state("X"):
            return depth - 10
        elif self.check_tie():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] is None:
                        self.board[row][col] = "O"
                        eval = self.minimax(depth + 1, False, alpha, beta)
                        self.board[row][col] = None
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] is None:
                        self.board[row][col] = "X"
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.board[row][col] = None
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, row, col):
        return self.check_winner_state(self.current_player)

    def check_winner_state(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)):
                return True
            if all(self.board[j][i] == player for j in range(self.size)):
                return True

        if all(self.board[i][i] == player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True

        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

root = tk.Tk()

# Set the board size here
board_size = 3

game = TicTacToe(root, board_size)
root.mainloop()
