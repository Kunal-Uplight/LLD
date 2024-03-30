from TicTacToe.strategies.winning_strategies.winning_strategy import WinningStrategy


class OrderOneColWinningStrategy(WinningStrategy):
    def __int__(self):
        pass

    def check_winner(self, board, move):
        # check columns
        for col in range(board.size):
            if all(board.cells[row][col].symbol == move.symbol for row in range(board.size)):
                return True
        return False



