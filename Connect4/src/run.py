
import os
import sys
from dotenv import load_dotenv, find_dotenv
import argparse

from logging import getLogger

from .helpers.logger import setup_logger
from .config import Config


logger = getLogger(__name__)

CMD_LIST = ['self', 'opt', 'eval', 'play_gui']
CMD_LIST_AF = ['relu', 'leakyrelu', 'sigmoid']

if find_dotenv():
    load_dotenv(find_dotenv())

_PATH_ = os.path.dirname(os.path.dirname(__file__))

if _PATH_ not in sys.path:
    sys.path.append(_PATH_)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="what to do", choices=CMD_LIST)
    parser.add_argument("--new", help="run from new best model", action="store_true")
    parser.add_argument("--type", help="use normal setting", default="normal")
    parser.add_argument("--total-step", help="set TrainerConfig.start_total_steps", type=int)
    parser.add_argument("--activation", help="which activation function to use", choices=CMD_LIST_AF, default="relu")
    return parser


def setup(config: Config, args):
    config.opts.new = args.new
    if args.total_step is not None:
        config.trainer.start_total_steps = args.total_step
    config.resource.create_directories()
    config.opts.activation = args.activation
    print("activation selected is!!!!!!!!!!", args.activation)

    if args.cmd == "self":
        setup_logger(config.resource.selfPlay_log_path)
    elif args.cmd == 'opt':
        setup_logger(config.resource.opt_log_path)
    elif args.cmd == 'eval':
        setup_logger(config.resource.eval_log_path)
    elif args.cmd == 'play_gui':
        setup_logger(config.resource.game_log_path)

    #setup_logger(config.resource.main_log_path)


def start():
    parser = create_parser()
    args = parser.parse_args()
    config_type = args.type

    config = Config(config_type=config_type)
    setup(config, args)

    logger.info(f"config type: {config_type}")

    if args.cmd == "self":
        from .modes import self_play
        return self_play.start(config)
    elif args.cmd == 'opt':
        from .modes import optimize
        return optimize.start(config)
    elif args.cmd == 'eval':
        from .modes import evaluate
        return evaluate.start(config)
    elif args.cmd == 'play_gui':
        from .connect4game import gui
        return gui.start(config)




if __name__ == "__main__":
    start()
