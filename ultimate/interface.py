import tkinter as tk
from tkinter import messagebox
import time

class GUI:
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
            if self.game.make_move(row, col, self.game.player_symbol) == True:
                self.buttons[row][col].config(text=self.game.player_symbol)

                if self.game.check_winner(self.game.player_symbol):
                    messagebox.showinfo('tk', "Win")
                    self.root.destroy()
                elif self.game.check_tie():
                    messagebox.showinfo('tk', "Tiee")
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
                messagebox.showinfo('tk',"Lose")
                self.root.destroy()
            elif self.game.check_tie():
                messagebox.showinfo('tk',"Tie")
                self.root.destroy()
            else:
                self.game.current_player = self.game.player_symbol

        print("AI's time to move: ", time.time() - start)
