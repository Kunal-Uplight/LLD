from cell import Cell


class Board:
    def __init__(self, size: int):
        self.size = size
        self.cells = self.__initialize_cells(size)

    @staticmethod
    def __initialize_cells(size: int):
        cells = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(i, j))
            cells.append(row)
        return cells
