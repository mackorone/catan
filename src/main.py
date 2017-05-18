from argparse import ArgumentParser
from board import Board
from config import Config
from size import InvalidSizeError


def main():
    parser = ArgumentParser(
        description='Settlers of Catan map generator',
    )
    parser.add_argument(
        '--height',
        type=int,
        default=5,
        help='must be positive',
    )
    parser.add_argument(
        '--width',
        type=int,
        default=5,
        help='must be positive, odd, and less than 2x height',
    )
    parser.add_argument(
        '--no-color',
        action='store_true',
        default=False,
        help='suppress terminal colors',
    )
    args = parser.parse_args()
    try:
        board = Board(args.height, args.width)
    except InvalidSizeError as e:
        print('Invalid size: {}'.format(e))
    except Exception as e:
        print('Unable to generate map: {}'.format(e))
    else:
        Config.NO_COLOR = args.no_color
        print(board)


if __name__ == '__main__':
    main()
