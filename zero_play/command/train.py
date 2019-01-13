import logging
from argparse import ArgumentDefaultsHelpFormatter
from itertools import count
from pathlib import Path
from random import shuffle

from zero_play.connect4.neural_net import NeuralNet
from zero_play.mcts_player import SearchManager
from zero_play.zero_play import CommandParser

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s:%(name)s: %(message)s")
    parser = CommandParser(description='Pit two players against each other.',
                           formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('game',
                        default='tictactoe',
                        help='the game to train for',
                        action='entry_point')
    parser.add_argument('--mcts_iterations',
                        type=int,
                        default=80,
                        help='the number of search iterations')
    parser.add_argument('--training_size',
                        type=int,
                        default=230,
                        help='the number of examples to generate')
    args = parser.parse_args()
    game = parser.load_argument(args, 'game')
    checkpoint_path = Path(f'data/{args.game}-nn')
    checkpoint_path.mkdir(parents=True, exist_ok=True)
    neural_net = NeuralNet(game)
    search_manager = SearchManager(game, neural_net)
    for i in count():
        logger.info('Creating training data.')
        training_data = search_manager.create_training_data(
            args.mcts_iterations,
            min_size=args.training_size)

        shuffle(training_data)
        filename = f'checkpoint-{i:02d}.pth.tar'
        logger.info('Training for %s.', filename)
        neural_net.train(training_data)
        neural_net.save_checkpoint(folder=checkpoint_path,
                                   filename=filename)
        search_manager.reset()


main()
