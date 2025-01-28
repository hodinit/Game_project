import tkinter as tk
from tkinter import messagebox
import math
import time

class TicTacToe:
    def __init__(self, size, player, ai):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = player

    def ai_move(self, game_board):
        start = time.time()

        best_score = -math.inf
        best_move = None

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == " ":
                    self.board[row][col] = self.current_player
                    score = self.minimax(0, False, -math.inf, math.inf)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.current_player
            game_board.update_button(row, col, self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", "You lost!")
                game_board.root.destroy()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                game_board.root.destroy()
            else:
                self.current_player = game_board.player

        print("AI move time:", time.time() - start)

    def minimax(self, depth, is_maximizing, alpha, beta):
        if depth > 6:
            return 0
        if self.check_winner(self.ai):
            return 10 - depth
        elif self.check_winner(self.player):
            return depth - 10
        elif self.check_tie():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] == " ":
                        self.board[row][col] = self.ai
                        eval = self.minimax(depth + 1, False, alpha, beta)
                        self.board[row][col] = " "
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] == " ":
                        self.board[row][col] = self.player
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.board[row][col] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, current_player):
        for row in range(self.size):
            if all(self.board[row][col] == current_player for col in range(self.size)):
                return True

        for col in range(self.size):
            if all(self.board[row][col] == current_player for row in range(self.size)):
                return True

        if all(self.board[i][i] == current_player for i in range(self.size)):
            return True

        if all(self.board[i][self.size - 1 - i] == current_player for i in range(self.size)):
            return True

        return False

    def check_tie(self):
        return all(self.board[row][col] != " " for row in range(self.size) for col in range(self.size))


