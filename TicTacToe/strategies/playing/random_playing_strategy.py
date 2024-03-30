import random

from TicTacToe.strategies.playing.playing_strategy import PlayingStrategy


class RandomPlayingStrategy(PlayingStrategy):
    def __int__(self, board=None):
        self.board = board

    def make_move(self, board):
        # get empty cells
        empty_cells = board.get_empty_cells()

        # randomly select a cell
        return random.choice(empty_cells)


