from winning_strategy import WinningStrategy


class OrderOneColWinningStrategy(WinningStrategy):
    def __int__(self, board, move):
        self.board = board
        self.move = move

    def check_winner(self, board, move):
        pass



