from TicTacToe.models.board import Board
from TicTacToe.models.bot_player import BotPlayer
from TicTacToe.models.game import Game
from TicTacToe.models.human_player import HumanPlayer
from TicTacToe.models.symbol import Symbol
from TicTacToe.models.user import User

BOARD_SIZE = 3


def test_game():
    players = [HumanPlayer(Symbol.X, User("user1", "test@test.com", "photo")),
               BotPlayer(Symbol.O, 1)]
    game = Game.builder().with_size(BOARD_SIZE).with_players(players).build()

    assert game.board.size == BOARD_SIZE, "Board size should be 3"
    assert len(game.players) == 2, "Number of players should be 2"


def test_create_board():
    board = Board(3)
    assert board.size == 3, "Board size should be 3"
    assert len(board.cells[0]) == 3, "Col size should be 3"
    # check column size
    assert len(board.cells) == 3, "Row size should be 3"
