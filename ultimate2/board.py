import tkinter as tk
from tkinter import messagebox

class GameBoard:
    def __init__(self, root, size, player, ai, game_logic):
        self.root = root
        self.size = size
        self.player = player
        self.ai = ai
        self.game_logic = game_logic

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
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
        if self.game_logic.board[row][col] == " " and self.game_logic.current_player == self.player:
            self.game_logic.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)

            if self.game_logic.check_winner(self.player):
                messagebox.showinfo("Tic Tac Toe", "You won!")
                self.root.destroy()
            elif self.game_logic.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.root.destroy()
            else:
                self.game_logic.current_player = self.ai
                self.game_logic.ai_move(self)

    def update_button(self, row, col, text):
        self.buttons[row][col].config(text=text)