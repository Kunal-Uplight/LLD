from winning_strategy import WinningStrategy


class OrderOneDiagWinningStrategy(WinningStrategy):
    def __int__(self, board, move):
        self.board = board
        self.move = move

    def check_winner(self, board, move):
        pass
