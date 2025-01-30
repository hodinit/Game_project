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
    # initializare interfata cu fereastra principala, jocul curent si AI-ul

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
    # metoda care creeaza butoanele pentru interfata, itereaza pe randuri 
    # si le adauga pe rand creand o matrice de butoane

    def on_click(self, row, col):
        if self.game.current_player == self.game.player_symbol:
            if self.game.make_move(row, col, self.game.player_symbol) == True:
                self.buttons[row][col].config(text=self.game.player_symbol)

                if self.game.check_winner(self.game.player_symbol):
                    messagebox.showinfo('Result', "Win")
                    self.root.destroy()
                elif self.game.check_tie():
                    messagebox.showinfo('Result', "Tiee")
                    self.root.destroy()
                else:
                    self.game.current_player = self.game.ai_symbol
                    self.ai_move()
    # metoda care se apeleaza cand se face click pe un buton si verifica daca jucatorul curent este omul
    # verifica daca mutarea este valida si pune simbolul jucatorului. ulterior verifica statusul jocului in caz ca s-a terminat,
    # iar daca nu ii vine randul AI-ului, schimband current_player si apeland metoda ai_move

    def ai_move(self):
        start = time.time()
        move = self.ai_player.find_best_move()

        if move != " ":
            row, col = move
            self.game.make_move(row, col, self.game.ai_symbol)
            self.buttons[row][col].config(text=self.game.ai_symbol)

            if self.game.check_winner(self.game.ai_symbol):
                messagebox.showinfo('Result',"Lose")
                self.root.destroy()
            elif self.game.check_tie():
                messagebox.showinfo('Result',"Tie")
                self.root.destroy()
            else:
                self.game.current_player = self.game.player_symbol

        print("AI's time taken to move: ", time.time() - start)
    # metoda care apeleaza metoda find_best_move ce returneaza un rand si o coloana stocate in move, apoi este verificat 
    # daca mutarea este valida si se pune simbolul AI-ului pe pozitie. ulterior se verifica statusul jocului si in caz
    # ca nu s-a terminat jocul se schimba current_player la jucatorul om. la final am facut o scadere intre timpul curent 
    # si cel stocat in start pentru a vedea cat timp a durat mutarea AI-ului.