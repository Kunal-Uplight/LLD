from TicTacToe.models.board import Board


def test_game():
    pass


def test_create_board():
    board = Board(3)
    assert board.size == 3, "Board size should be 3"
    assert len(board.cells[0]) == 3, "Col size should be 3"
    # check column size
    assert len(board.cells) == 3, "Row size should be 3"
