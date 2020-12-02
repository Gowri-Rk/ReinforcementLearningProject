"""
Main entry point for running from command line.
Manages starting off each of the separate processes involved -
self play, training, and evaluation.

"""

import os
import sys
import multiprocessing as mp
import argparse

from logging import getLogger,disable

from lib.logger import setup_logger
from lib.config import Config

_PATH_ = os.path.dirname(os.path.dirname(__file__))

if _PATH_ not in sys.path:
    sys.path.append(_PATH_)

logger = getLogger(__name__)

CMD_LIST = ['self-play', 'optimize', 'evaluate', 'supervised', 'game']
ACT_LIST = ['relu', 'leakyrelu', 'sigmoid']


def create_parser():
    """
    Parses each of the arguments from the command line
    :return ArgumentParser representing the command line arguments that were supplied to the command line:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--cmd", help="what to do", choices=CMD_LIST)
    parser.add_argument("--new", help="run from new best model", action="store_true")
    parser.add_argument("--activation", help="whiich activation function to use", choices=ACT_LIST, default="relu")

    return parser


def setup(config: Config, args):
    """
    Sets up a new config by creating the required directories and setting up logging.

    :param Config config: config to create directories for and to set config from based on the args
    :param ArgumentParser args: args to use to control config.
    """
    config.opts.new = args.new
    config.opts.activation = args.activation
    config.resource.create_directories()
    setup_logger(config.resource.main_log_path)


def start():
    """
    Start one of the processes based on command line arguments.
    """
    parser = create_parser()
    args = parser.parse_args()


    config = Config()
    setup(config, args)

    if args.cmd == 'self-play':
        from agz_commands import self_play
        return self_play.start(config)
    elif args.cmd == 'optimize':
        from agz_commands import optimize
        return optimize.start(config)
    elif args.cmd == 'evaluate':
        from agz_commands import evaluate
        return evaluate.start(config)
    elif args.cmd == 'supervised':
        from agz_commands import supervised
        return supervised.start(config)
    elif args.cmd == 'game':
        from game import game
        return game.start(config) 

if __name__ == "__main__":
    mp.set_start_method('spawn')
    sys.setrecursionlimit(10000)
    start()
