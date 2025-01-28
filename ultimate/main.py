import tkinter as tk
from game_logic import TicTacToe
from ai import AI
from interface import GUI

if __name__ == "__main__":
    root = tk.Tk()
    board_size = 4
    player_symbol = "X"
    ai_symbol = "O"

    game = TicTacToe(board_size, player_symbol, ai_symbol)
    ai_player = AI(game)
    app = GUI(root, game, ai_player)
    root.mainloop()
