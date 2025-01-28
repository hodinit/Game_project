import tkinter as tk
from game_logic import TicTacToe
from board import GameBoard

if __name__ == "__main__":
    root = tk.Tk()
    board_size = 4
    player_symbol = "X"
    ai_symbol = "O"
    game_logic = TicTacToe(board_size, player_symbol, ai_symbol)
    game_board = GameBoard(root, board_size, player_symbol, ai_symbol, game_logic)
    root.mainloop()