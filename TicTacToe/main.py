# Client code for tic tac toe game

from TicTacToe.models.bot_player import BotPlayer
from TicTacToe.models.game import Game
from TicTacToe.models.game_status import GameStatus
from TicTacToe.models.human_player import HumanPlayer
from TicTacToe.models.symbol import Symbol
from TicTacToe.models.user import User
from TicTacToe.strategies.winning_strategies.order_one_col_winning_strategy import OrderOneColWinningStrategy
from TicTacToe.strategies.winning_strategies.order_one_diag_winning_strategy import OrderOneDiagWinningStrategy
from TicTacToe.strategies.winning_strategies.order_one_row_winning_strategy import OrderOneRowWinningStrategy


def get_human_player():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    symbol = input("Enter your Symbol: ")

    user = User(name, email, None)

    try:
        symbol = Symbol(symbol)
    except ValueError as e:
        print("Invalid Symbol. Please enter a valid symbol")
        return

    return HumanPlayer(symbol, user)


def create_game(human_player: HumanPlayer):
    players = [human_player, BotPlayer(decide_bot_symbol(human_player), 1)]
    winning_strategies = [OrderOneRowWinningStrategy(), OrderOneColWinningStrategy(), OrderOneDiagWinningStrategy()]
    game = Game.builder().with_size(3).with_players(players).with_winning_strategies(winning_strategies).build()
    return game


def decide_bot_symbol(human_player: HumanPlayer):
    return Symbol.X if human_player.symbol == Symbol.O else Symbol.O


if __name__ == "__main__":
    print("Welcome to TicTacToe")

    human_player = get_human_player()
    if not human_player:
        print("Invalid player. Exiting game")
        exit()

    print("Welcome, ", human_player.user.name, "!", "Your symbol is: ", human_player.symbol)

    game = create_game(human_player)

    game.start()

    while game.game_status == GameStatus.IN_PROGRESS:
        player = game.get_next_player()
        print("Next player: ", player.symbol)
        game.make_move()
        game.board.print_board()

    if game.game_status == GameStatus.FINISHED:
        if game.winner:
            print("Winner is: ", game.winner.symbol)
        elif game.is_draw():
            print("Game is a draw")

