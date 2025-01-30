import math

class AI:
    def __init__(self, game):
        self.game = game
    # initializare AI cu instanta jocului curent

    def find_best_move(self):
        best_score = -math.inf
        best_move = " "

        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board[row][col] == " ":
                    self.game.board[row][col] = self.game.ai_symbol
                    score = self.minimax(0, False, -math.inf, math.inf)
                    self.game.board[row][col] = " "

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move
    # metoda care gaseste cea mai buna mutare pentru AI astfel: initializam best_score cu -infinit pentru a ne
    # asigura ca orice mutare gasita si calculata de minimax va avea un scor mai mare ca aceasta valoare
    # si se vor updata best_score si best_move. 
    # cu ajutorul for loop-urilor iteram pe pozitiile libere ale ablei si cand o gasim punem simbolul AI
    # pentru a o marca ca o posibila mutare.
    # apelam minimax cu adancimea setata la 0, is_maximizing False, alpha -infinit si beta infinit, 
    # dupa care minimax evalueaza pozitia curenta. dupa evaluare, pozitia se reseteaza si se verifica 
    # daca scorul rezultat este mai mare ca best_score, si daca da, best_score si best_move se updateaza. 
    # acest proces se repeta pana cand toate pozitiile sunt verificate si la final se returneaza best_move 

    def minimax(self, depth, is_maximizing, alpha, beta):
        if depth>6:
            return 0
        if self.game.check_winner(self.game.ai_symbol) == True:
            return 10-depth
        if self.game.check_winner(self.game.player_symbol) == True:
            return depth-10
        if self.game.check_tie() == True:
            return 0

        if is_maximizing == True:
            max_eval = -math.inf
            for row in range(self.game.size):
                for col in range(self.game.size):
                    if self.game.board[row][col] == " ":
                        self.game.board[row][col] = self.game.ai_symbol
                        eval = self.minimax(depth+1, False, alpha, beta)
                        self.game.board[row][col] = " "
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.game.size):
                for col in range(self.game.size):
                    if self.game.board[row][col] == " ":
                        self.game.board[row][col] = self.game.player_symbol
                        eval = self.minimax(depth+1, True, alpha, beta)
                        self.game.board[row][col] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval
        
    # metoda minimax evalueaza pozitia curenta si returneaza un scor. primul if (depth>6) este 
    # pentru a limita cautarea in adancime pentru a permite rularea intr-un timp rezonabil. 
    # la celelalte if-uri, daca AI-ul castiga returneaza un scor pozitiv, daca jucaorul castiga
    # returneaza un scor negativ, iar daca e remiza returneaza 0. 
    # logica minimax: daca se maximizeaza, se initializeaza max_eval cu -infinit, se itereaza pe toate
    # pozitiile libere se pune simbolul AI-ului preventiv, se apeleaza recursiv minimax cu is_maximizing
    # setat pe False pentru ca la reapelare sa evalueze is_maximizings cu False si sa mearga pe else unde
    # sa simuleze mutarea jucatorului presupunand ca joaca optim. se evalueaza pozitia si se reseteaza.
    # se updateaza max_eval cu maximul dintre max_eval si eval. alpha se updateaza cu maximul dintre alpha si eval.
    # daca beta e mai mic sau egal cu alpha se iese din loop. acest lucru asigura optimizarea pentru ca 
    # atunci cand se vrea sa se maximizeze si scorul dintr-un nod e mai mic decat celalalt, algoritmul 
    # nu va parcurge restul arborelui stiind ca mergand pe celalalt nod va avea un scor garantat mai mare.
    # la final se returneaza max_eval.
    # pe partea cealalta, daca se minimizeaza procesul este similar doar ca min_eval e initializat
    # cu infinit si se updateaza cu minimul dintre min_eval si eval. un alt aspect important este
    # setarea is_maximizing la True la apelarea minimax pentru a ne asigura ca la urmatoarea reapelare
    # merge pe mutarea AI-ului. la optimizare beta se updateaza cu minimul dintre beta si eval si daca
    # beta e mai mic sau egal cu alpha loopul se termina si la final se returneaza min_eval.
    # practic acest proces simuleaza un joc turn-based intre 2 jucatori
    # acest proces se repeta pana cand se ajunge la o frunza a arborelui