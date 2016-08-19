from board import Board
from graphics import UI
from resource import Resource


def main():
    board = Board(
        height=5,
        width=5,
    )
    print(UI(board))

if __name__ == '__main__':
    main()
