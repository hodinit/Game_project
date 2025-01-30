class TicTacToe: 
    def __init__(self, size, player_symbol, ai_symbol): 
        self.size = size 
        self.board=[] 
        for i in range(size): 
            row=[]
            for j in range(size):
                row.append(" ")
            self.board.append(row)
            
        self.player_symbol = player_symbol 
        self.ai_symbol = ai_symbol 
        self.current_player = player_symbol 
    # initializare joc cu parametrii din constructor, o tabla vida ce contine spatii goale si
    # si currenr_player care ia simbolul jucatorului
 
    def make_move(self, row, col, current_player): 
        if self.board[row][col] == " ": 
            self.board[row][col] = current_player 
            return True 
        return False 
    # metoda pentru a face o mutare care verifica daca pozitia este vida si daca da primeste simbolul jucatorului curent, 
    # dupa care returneaza True daca mutarea a fost facuta si False daca nu 

    def check_winner(self, current_player):
        for i in range(self.size):
            count=0
            for j in range(self.size):
                if self.board[i][j] == current_player:
                    count+=1
                else:
                    break
            if count == self.size:
                return True
        # for loop care itereaza pe linii si ia un count care creste daca gaseste simbolul jucatorului curent si 
        # daca e egal cu dimensiunea tablei returneaza True

        for j in range(self.size):
            count=0
            for i in range(self.size):
                if self.board[i][j] == current_player:
                    count+=1
                else:
                    break
            if count == self.size:
                return True
        # for loop asemanator cu celalalt care itereaza pe coloane si ia un count care creste daca gaseste simbolul jucatorului curent si 
        # daca e egal cu dimensiunea tablei returneaza True

        count=0
        for i in range(self.size):
            if self.board[i][i] == current_player:
                count+=1
            else:
                break
        if count == self.size:
            return True
        # for loop care itereaza pe diagonala principala si ia un count care creste daca gaseste
        # simbolul jucatorului curent si il verifica cu dimensiunea tablei si returneaza True daca e adevarat

        count=0
        for i in range(self.size):
            if self.board[i][self.size-1-i] == current_player:
                count+=1
            else:
                break
        if count == self.size:
            return True
        # for loop asemanator cu cel anterior care itereaza pe diagonala secundara
        # si ia un count care creste daca gaseste simbolul jucatorului curent si e egal cu dimensiunea returneaza True

        return False # returneaza False daca nu a gasit niciun castigator

    def check_tie(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    return False
        return True
    # metoda care verifica daca mai sunt spatii goale pe tabla si daca nu returneaza True
