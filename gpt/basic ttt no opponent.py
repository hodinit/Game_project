import tkinter as tk
from tkinter import messagebox
import math
import time

class TicTacToe:
    def __init__(self, root, size, player, ai):
        self.root=root
        self.size=size
        self.board=[]
        for i in range(size):
            row=[]
            for j in range(size):
                row.append(" ")
            self.board.append(row)

        self.current_player = player
        self.create_widgets(player, ai)

    def create_widgets(self, player, ai):
        self.buttons =[]

        for row in range(self.size):
            button_row =[]
            for col in range(self.size):
                button =tk.Button(
                    self.root,
                    height=5,
                    width=10,
                    command=lambda r=row, c=col: self.on_click(r, c, player, ai)
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def on_click(self, row, col, player, ai):
        if self.board[row][col] == " " and self.current_player == player:
            self.board[row][col]=self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo("tk","Ai castigat")
                self.root.destroy()
            elif self.check_tie():
                messagebox.showinfo("tk","Egalitate")
                self.root.destroy()
            else:
                self.current_player= ai
                self.ai_move(player, ai)

    def ai_move(self, player, ai):
        start=time.time()

        best_score = -math.inf
        best_move = " "

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == " ":
                    self.board[row][col] = ai
                    score = self.minimax(0, False, -math.inf, math.inf, player, ai)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score =score
                        best_move =(row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = ai
            self.buttons[row][col].config(text=ai)

            if self.check_winner(ai):
                messagebox.showinfo("tk","Ai pierdut")
                self.root.destroy()
            elif self.check_tie():
                messagebox.showinfo("tk","Egalitate")
                self.root.destroy()
            else:
                self.current_player = player

        print("Timp necesar AI pentru mutare: ", time.time()-start)

    def minimax(self, depth, is_maximizing, alpha, beta, player, ai):
        if depth>6: # explain
            return 0
        if self.check_winner(ai):
            return 10-depth
        elif self.check_winner(player):
            return depth-10
        elif self.check_tie():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] ==" ":
                        self.board[row][col] =ai
                        eval=self.minimax(depth + 1, False, alpha, beta, player, ai)
                        self.board[row][col] =" "
                        max_eval=max(max_eval, eval)
                        alpha=max(alpha, eval)
                        if beta <=alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] ==" ":
                        self.board[row][col] =player
                        eval=self.minimax(depth + 1, True, alpha, beta, player, ai)
                        self.board[row][col] =" "
                        min_eval=min(min_eval, eval)
                        beta=min(beta, eval)
                        if beta <=alpha:
                            break
            return min_eval

    def check_winner(self, current_player):
        for row in range(self.size):
            count=0
            for col in range(self.size):
                if self.board[row][col] == current_player:
                    count+=1
                else:
                    break
            if count == self.size:
                return True

        for col in range(self.size):
            count=0
            for row in range(self.size):
                if self.board[row][col] == current_player:
                    count+=1
                else:
                    break
            if count == self.size:
                return True

        count=0
        for i in range(self.size):
            if self.board[i][i] == current_player:
                count+=1
            else:
                break
        if count == self.size:
            return True

        count=0
        for i in range(self.size):
            if self.board[i][self.size-1-i] == current_player:
                count+=1
            else:
                break
        if count == self.size:
            return True

        return False

    def check_tie(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    return False
        return True


root = tk.Tk()

board_size = 4
player_symbol = "X"
ai_symbol = "O"

game = TicTacToe(root, board_size, player_symbol, ai_symbol)
root.mainloop()
