from typing import List

from board import Board
from game_status import GameStatus
from player import Player


class Game:
    def __int__(self, board: Board, players: List[Player], winning_strategies):
        self.moves = []  # internal state, when the game is created we don't have this
        self.board = board
        self.players = players
        self.current_player_move_idx = 0
        self.winning_strategies = winning_strategies
        self.game_status = GameStatus.IN_PROGRESS
        self.winner = None

    def make_move(self, row, col):
        pass

    def start(self):
        pass

    def is_winner(self, player):
        pass

    def is_draw(self):
        pass


