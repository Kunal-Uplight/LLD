from TicTacToe.strategies.winning_strategies.winning_strategy import WinningStrategy


class OrderOneDiagWinningStrategy(WinningStrategy):
    def __int__(self):
        pass

    def check_winner(self, board, move):
        # check diagonals
        if all(board.cells[i][i].symbol == move.symbol for i in range(board.size)):
            return True
