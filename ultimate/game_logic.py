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

    def make_move(self, row, col, current_player):
        if self.board[row][col] == " ":
            self.board[row][col] = current_player
            return True
        return False

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
