from board import Board
from resource import Resource


def main():
    b = Board(size=2)
    print(b)
    # for i in range(200):
    #     print('\033[{0}m{0}'.format(i))

if __name__ == '__main__':
    main()
