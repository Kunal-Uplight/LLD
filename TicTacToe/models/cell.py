from cell_state import CellState


class Cell:
    def __init__(self, row, col, player=None):
        self.row = row
        self.col = col
        self.cell_state = CellState.EMPTY
        self.player = player
