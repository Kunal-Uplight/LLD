from random import randint
from typing import List

from TicTacToe.models.board import Board
from TicTacToe.models.game_status import GameStatus
from TicTacToe.models.player import Player


class Game:
    def __int__(self, board: Board = None, players: List[Player] = None, winning_strategies=None):
        self.moves = []  # internal state, when the game is created we don't have this
        self.board = board
        self.players = players
        self.current_player_move_idx = 0
        self.winning_strategies = winning_strategies
        self.game_status = GameStatus.IN_PROGRESS
        self.winner = None

    def make_move(self):
        # get next move from current player
        move = self.get_next_move()

        # validate move
        self.validate_move(move)

        # update board
        self.board.update_cell(move)

        # check for winner
        if self.is_winner(self.board, move):
            self.game_status = GameStatus.FINISHED
            return

        # check for draw
        if self.is_draw():
            self.game_status = GameStatus.FINISHED
            return

        # update current player
        self.current_player_move_idx = (self.current_player_move_idx + 1) % len(self.players)

    def get_next_move(self):
        player = self.players[self.current_player_move_idx]
        return player.make_move(self.board)

    def get_next_player(self):
        return self.players[self.current_player_move_idx]

    def validate_move(self, move):
        is_empty = self.board.is_empty(move.row, move.col)
        if not is_empty:
            raise ValueError("Cell- [{}, {}] is already occupied".format(move.row, move.col))

    def start(self):
        self.current_player_move_idx = randint(0, len(self.players) - 1)

    def is_winner(self, board, move):
        for strategy in self.winning_strategies:
            if strategy.check_winner(board, move):
                self.winner = self.players[self.current_player_move_idx]
                return True
        return False

    def is_draw(self):
        empty_cells = self.board.get_empty_cells()
        return not empty_cells

    @staticmethod
    def builder():
        return Game.Builder()

    class Builder:
        def __init__(self):
            self.game = Game()

        def with_size(self, size: int):
            self.game.board = Board(size)
            return self

        def with_players(self, players: List[Player]):
            self.game.players = players
            return self

        def with_winning_strategies(self, winning_strategies):
            self.game.winning_strategies = winning_strategies
            return self

        def build(self):
            self.validate()
            new_game = Game()
            new_game.board = self.game.board
            new_game.players = self.game.players
            new_game.game_status = GameStatus.IN_PROGRESS
            new_game.winning_strategies = self.game.winning_strategies

            return new_game

        def validate(self):
            # check number of players
            if len(self.game.players) < 2:
                raise ValueError("At least 2 players are required")

            # check unique symbols
            symbols = {player.symbol for player in self.game.players}
            if len(symbols) != len(self.game.players):
                raise ValueError("Players should have unique symbols")

            return True
