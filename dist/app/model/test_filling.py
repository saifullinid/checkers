from .Checker import BlackChecker, WhiteChecker


def test_filling_board_1(board):
    blackcoords = [
        # [0, 1, 0],
        # [0, 3, 0],
        # [0, 5, 0],
        # [0, 7, 0],

        # [1, 0, 0],
        # [1, 2, 0],
        # [1, 4, 0],
        # [1, 6, 0],

        # [2, 1, 0],
        # [2, 3, 0],
        # [2, 5, 0],
        # [2, 7, 0],

        # [3, 0, 0],
        # [3, 2, 0],
        # [3, 4, 0],
        # [3, 6, 0],

        # [4, 1, 0],
        # [4, 3, 0],
        [4, 5, 0],
        # [4, 7, 0],

        # [5, 0, 0],
        # [5, 2, 0],
        # [5, 4, 0],
        # [5, 6, 0],

        # [6, 1, 0],
        # [6, 3, 0],
        # [6, 5, 0],
        # [6, 7, 0],

        # [7, 0, 0],
        # [7, 2, 0],
        [7, 4, 1], # queen
        # [7, 6, 0],
    ]

    for row, column, rank in blackcoords:
        key = (row, column)
        board.field[key] = BlackChecker(row, column, rank)

    emptycoords = [
        [0, 1, 0],
        [0, 3, 0],
        [0, 5, 0],
        [0, 7, 0],

        [1, 0, 0],
        [1, 2, 0],
        [1, 4, 0],
        [1, 6, 0],

        [2, 1, 0],
        [2, 3, 0],
        [2, 5, 0],
        [2, 7, 0],

        [3, 0, 0],
        [3, 2, 0],
        [3, 4, 0],
        [3, 6, 0],

        [4, 1, 0],
        [4, 3, 0],
        # [4, 5, 0],
        [4, 7, 0],

        [5, 0, 0],
        # [5, 2, 0],
        [5, 4, 0],
        [5, 6, 0],

        [6, 1, 0],
        # [6, 3, 0],
        [6, 5, 0],
        [6, 7, 0],

        [7, 0, 0],
        [7, 2, 0],
        # [7, 4, 0],
        [7, 6, 0],
    ]
    for row, column, rank in emptycoords:
        key = (row, column)
        board.field[key] = 'empty'

    whitecoords = [
        # [0, 1, 0],
        # [0, 3, 0],
        # [0, 5, 0],
        # [0, 7, 0],

        # [1, 0, 0],
        # [1, 2, 0],
        # [1, 4, 0],
        # [1, 6, 0],

        # [2, 1, 0],
        # [2, 3, 0],
        # [2, 5, 0],
        # [2, 7, 0],

        # [3, 0, 0],
        # [3, 2, 0],
        # [3, 4, 0],
        # [3, 6, 0],

        # [4, 1, 0],
        # [4, 3, 0],
        # [4, 5, 0],
        # [4, 7, 0],

        # [5, 0, 0],
        [5, 2, 0],
        # [5, 4, 0],
        # [5, 6, 0],

        # [6, 1, 0],
        [6, 3, 0],
        # [6, 5, 0],
        # [6, 7, 0],

        # [7, 0, 0],
        # [7, 2, 0],
        # [7, 4, 0],
        # [7, 6, 0],
    ]
    for row, column, rank in whitecoords:
        key = (row, column)
        board.field[key] = WhiteChecker(row, column, rank)