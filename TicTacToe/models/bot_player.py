from TicTacToe.models.board import Board
from TicTacToe.models.cell import Cell
from TicTacToe.models.player import Player
from TicTacToe.strategies.playing.random_playing_strategy import RandomPlayingStrategy


class BotPlayer(Player):
    def __init__(self, symbol, difficulty_level):
        super().__init__(symbol)
        self.difficulty_level = difficulty_level
        self.playing_strategy = RandomPlayingStrategy()

    def make_move(self, board: Board) -> Cell:
        cell = self.playing_strategy.make_move(board)
        return Cell(cell.row, cell.col, self.symbol)
