About
=====

Connect4 reinforcement learning by [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/) methods.

This project is based in two main resources:
1) DeepMind's Oct19th publication: [Mastering the Game of Go without Human Knowledge](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ).
2) The <b>great</b> Reversi development of the DeepMind ideas that @mokemokechicken did in his repo: https://github.com/mokemokechicken/reversi-alpha-zero
3) https://github.com/Zeta36/connect4-alpha-zero

Environment
-----------

* Python 3.6.3
* tensorflow-gpu: 1.3.0
* Keras: 2.0.8


Commands
-----------------

Self-Play
python src/connect4_zero/run.py self

Trainer
python src/connect4_zero/run.py opt


Evaluator
python src/connect4_zero/run.py eval


Game Play
python src/connect4_zero/run.py eval
