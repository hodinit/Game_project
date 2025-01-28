import tkinter as tk
from tkinter import messagebox
import math
import time

class TicTacToeGame:
    def __init__(self, size, player_symbol, ai_symbol):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.player_symbol = player_symbol
        self.ai_symbol = ai_symbol
        self.current_player = player_symbol

    def make_move(self, row, col, symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.board[row][col] == symbol for row in range(self.size)):
                return True

        # Check main diagonal
        if all(self.board[i][i] == symbol for i in range(self.size)):
            return True

        # Check anti-diagonal
        if all(self.board[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True

        return False

    def check_tie(self):
        return all(cell != " " for row in self.board for cell in row)

class AIPlayer:
    def __init__(self, game):
        self.game = game

    def find_best_move(self, depth_limit=6):
        best_score = -math.inf
        best_move = None

        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board[row][col] == " ":
                    self.game.board[row][col] = self.game.ai_symbol
                    score = self.minimax(0, False, -math.inf, math.inf, depth_limit)
                    self.game.board[row][col] = " "

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, depth, is_maximizing, alpha, beta, depth_limit):
        if depth > depth_limit:
            return 0

        if self.game.check_winner(self.game.ai_symbol):
            return 10 - depth

        if self.game.check_winner(self.game.player_symbol):
            return depth - 10

        if self.game.check_tie():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row in range(self.game.size):
                for col in range(self.game.size):
                    if self.game.board[row][col] == " ":
                        self.game.board[row][col] = self.game.ai_symbol
                        eval = self.minimax(depth + 1, False, alpha, beta, depth_limit)
                        self.game.board[row][col] = " "
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.game.size):
                for col in range(self.game.size):
                    if self.game.board[row][col] == " ":
                        self.game.board[row][col] = self.game.player_symbol
                        eval = self.minimax(depth + 1, True, alpha, beta, depth_limit)
                        self.game.board[row][col] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

class TicTacToeUI:
    def __init__(self, root, game, ai_player):
        self.root = root
        self.game = game
        self.ai_player = ai_player
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        for row in range(self.game.size):
            button_row = []
            for col in range(self.game.size):
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
        if self.game.current_player == self.game.player_symbol:
            if self.game.make_move(row, col, self.game.player_symbol):
                self.buttons[row][col].config(text=self.game.player_symbol)

                if self.game.check_winner(self.game.player_symbol):
                    messagebox.showinfo("Game Over", "You Win!")
                    self.root.destroy()
                elif self.game.check_tie():
                    messagebox.showinfo("Game Over", "It's a Tie!")
                    self.root.destroy()
                else:
                    self.game.current_player = self.game.ai_symbol
                    self.ai_move()

    def ai_move(self):
        start = time.time()
        move = self.ai_player.find_best_move()

        if move:
            row, col = move
            self.game.make_move(row, col, self.game.ai_symbol)
            self.buttons[row][col].config(text=self.game.ai_symbol)

            if self.game.check_winner(self.game.ai_symbol):
                messagebox.showinfo("Game Over", "You Lose!")
                self.root.destroy()
            elif self.game.check_tie():
                messagebox.showinfo("Game Over", "It's a Tie!")
                self.root.destroy()
            else:
                self.game.current_player = self.game.player_symbol

        print("AI move time:", time.time() - start)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    board_size = 4
    player_symbol = "X"
    ai_symbol = "O"

    game = TicTacToeGame(board_size, player_symbol, ai_symbol)
    ai_player = AIPlayer(game)
    app = TicTacToeUI(root, game, ai_player)
    root.mainloop()
