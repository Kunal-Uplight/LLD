from TicTacToe.models.difficulty_level import DifficultyLevel
from hard_bot_playing_strategy import HardBotPlayingStrategy
from medium_bot_playing_strategy import MediumBotPlayingStrategy
from random_playing_strategy import EasyBotPlayingStrategy


class BotPlayingStrategyFactory:
    def __int__(self):
        pass

    @staticmethod
    def get_bot_playing_strategy(difficulty_level):
        if difficulty_level == DifficultyLevel.MEDIUM:
            return MediumBotPlayingStrategy()
        elif difficulty_level == DifficultyLevel.HARD:
            return HardBotPlayingStrategy()
        else:
            return EasyBotPlayingStrategy()
