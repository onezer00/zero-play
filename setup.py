"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup
from os import path
import zero_play

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='zero_play',
      version=zero_play.__version__,
      description='Play board games using the techniques from AlphaZero',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/donkirkby/zero-play',
      author='Don Kirkby',
      classifiers=[  # https://pypi.org/classifiers/
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Games/Entertainment :: Board Games',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.8'],
      keywords='boardgames alphazero machine learning mcts',
      packages=['zero_play'],
      install_requires=['numpy', 'tensorflow', 'PySide2'],
      extras_require={'dev': ['seaborn',
                              'matplotlib',
                              'numpy',
                              'pytest',
                              'coverage',
                              'mypy'],
                      'gpu': ['tensorflow-gpu']},
      entry_points={
          'console_scripts': ['zero_play=zero_play.zero_play:main'],
          'gui_scripts': ['zero_play_gui=zero_play.zero_play_gui:main'],
          # The game entry point lets you add rules for new games.
          # The zero_play.game.Game class is a useful base class.
          'zero_play.game': ['tictactoe=zero_play.tictactoe.game:TicTacToeGame',
                             'connect4=zero_play.connect4.game:Connect4Game',
                             'othello=zero_play.othello.game:OthelloGame'],
          # The game_display entry point lets you add screens for new games.
          # The zero_play.game_display.GameDisplay class is a useful base class.
          'zero_play.game_display': [
              'tictactoe=zero_play.tictactoe.display:TicTacToeDisplay',
              'connect4=zero_play.connect4.display:Connect4Display',
              'othello=zero_play.othello.display:OthelloDisplay'],
          # The player entry point lets you add new ways to choose moves.
          # The zero_play.player.Player class is a useful base class.
          'zero_play.player': ['human=zero_play.human_player:HumanPlayer',
                               'mcts=zero_play.mcts_player:MctsPlayer'],
          # The heuristic entry point lets you add new ways to evaluate boards.
          # Playout is general purpose, and the others are custom neural
          # networks for each game.
          'zero_play.heuristic': ['playout=zero_play.playout:Playout',
                                  'connect4=zero_play.connect4.neural_net:NeuralNet']},
      project_urls={
          'Bug Reports': 'https://github.com/donkirkby/zero-play/issues',
          'Source': 'https://github.com/donkirkby/zero-play'})
