from TicTacToe.strategies.winning_strategies.winning_strategy import WinningStrategy


class OrderOneRowWinningStrategy(WinningStrategy):
    def __int__(self):
        pass

    def check_winner(self, board, move):
        # check rows
        for row in board.cells:
            if all(cell.symbol == move.symbol for cell in row):
                return True
        return False
