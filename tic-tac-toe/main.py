import tkinter as tk
from game_logic import TicTacToe
from ai import AI
from interface import GUI
# importare libraria tkinter si clase din alte fisiere

root = tk.Tk() # initializare fereastra principala tkinter
board_size = 4 # setare dimensiune tabla
player_symbol = "X" # setare simbol jucator
ai_symbol = "O" # setare simbol AI

game = TicTacToe(board_size, player_symbol, ai_symbol) # initializare joc 
ai = AI(game) # initializare AI
app = GUI(root, game, ai) # initializare interfata
root.mainloop() # sintaxa specifica tkinter pentru rulare interfata
