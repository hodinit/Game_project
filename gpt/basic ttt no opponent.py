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
        if self.board[row][col] is None:  # Check if the cell is empty
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.destroy()
            else:
                tie = True
                for row in self.board:
                    for cell in row:
                        if cell is None:
                            tie = False
                            break
                    if tie == False:
                        break
                if tie == True:
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.root.destroy()
                else:
                    if self.current_player == "X":
                        self.current_player = "O"
                    else:
                        self.current_player = "X" 

    def check_winner(self, row, col):
        # Check row
        row_win = True
        for c in range(self.size):
            if self.board[row][c] != self.current_player:
                row_win = False
                break
        if row_win == True:
            return True

        # Check column
        col_win = True
        for r in range(self.size):
            if self.board[r][col] != self.current_player:
                col_win = False
                break
        if col_win == True:
            return True

        # Check main diagonal
    
        diag_win = True
        for i in range(self.size):
            if self.board[i][i] != self.current_player:
                diag_win = False
                break
        if diag_win == True:
            return True

        # Check anti-diagonal
        anti_diag_win = True
        for i in range(self.size):
            if self.board[i][self.size - 1 - i] != self.current_player:
                anti_diag_win = False
                break
        if anti_diag_win:
            return True

        return False

    # def reset_board(self):
    #     self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
    #     for row in self.buttons:
    #         for button in row:
    #             button.config(text="")
    #     self.current_player = "X"


root = tk.Tk()

# Set the board size here
board_size = 3

game = TicTacToe(root, board_size)
root.mainloop()
