from TicTacToe.models.cell import Cell


class Board:
    def __init__(self, size: int):
        self.size = size
        self.cells = self.__initialize_cells(size)

    @staticmethod
    def __initialize_cells(size: int) -> list[list[Cell]]:
        cells = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(i, j, ""))
            cells.append(row)
        return cells

    def is_empty(self, row, col):
        return not bool(self.cells[row][col].symbol)

    def update_cell(self, move: Cell):
        self.cells[move.row][move.col].symbol = move.symbol

    def print_board(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol.name if cell.symbol else "_", end=" ")
            print()
        print()

    def get_empty_cells(self):
        empty_cells = []
        for row in self.cells:
            for cell in row:
                if not cell.symbol:
                    empty_cells.append(cell)
        return empty_cells
