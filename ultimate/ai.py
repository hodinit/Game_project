import math

class AIPlayer:
    def __init__(self, game):
        self.game = game

    def find_best_move(self):
        best_score = -math.inf
        best_move = None

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

    def minimax(self, depth, is_maximizing, alpha, beta):
        if depth > 6:
            return 0

        if self.game.check_winner(self.game.ai_symbol):
            return 10 - depth

        if self.game.check_winner(self.game.player_symbol):
            return depth - 10

        if self.game.check_tie():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row in range(self.game.size):
                for col in range(self.game.size):
                    if self.game.board[row][col] == " ":
                        self.game.board[row][col] = self.game.ai_symbol
                        eval = self.minimax(depth + 1, False, alpha, beta)
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
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.game.board[row][col] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval
