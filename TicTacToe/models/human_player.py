from TicTacToe.models.board import Board
from TicTacToe.models.cell import Cell
from TicTacToe.models.player import Player
from TicTacToe.models.symbol import Symbol
from TicTacToe.models.user import User


class HumanPlayer(Player):
    def __init__(self, symbol: Symbol, user: User):
        super().__init__(symbol)
        self.user = user

    def make_move(self, board: Board) -> Cell:
        # Implementation for human player's play method
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        return Cell(row, col, self.symbol)
