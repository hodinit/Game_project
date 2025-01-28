import tkinter as tk
from game_logic import TicTacToeGame
from ai import AIPlayer
from ui import TicTacToeUI

if __name__ == "__main__":
    root = tk.Tk()
    board_size = 4
    player_symbol = "X"
    ai_symbol = "O"

    game = TicTacToeGame(board_size, player_symbol, ai_symbol)
    ai_player = AIPlayer(game)
    app = TicTacToeUI(root, game, ai_player)
    root.mainloop()
