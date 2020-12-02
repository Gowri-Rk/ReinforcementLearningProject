from logging import getLogger

import chess
from lib.config import Config, DemoConfig
from game.game_model import PlayWithHuman
from env.chess_env import ChessEnv
from random import random

logger = getLogger(__name__)


def start(config: Config):
    DemoConfig().update_play_config(config.play)
    chess_model = PlayWithHuman(config)

    env = ChessEnv(config).reset()
    human_is_black = random() < 0.5
    chess_model.start_game(human_is_black)

    while not env.done:
        if (env.board.turn == chess.BLACK) == human_is_black:
            action = chess_model.move_by_human(env)
            print("You move to: " + action)
        else:
            action = chess_model.move_by_ai(env)
            print("AI moves to: " + action)
        env.step(action)
        env.render()
        print("Board FEN = " + env.board.fen())

    print("\nEnd of the game.")
    print("Game result:")
    print(env.board.result())