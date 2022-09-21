# from .Board import Board
from .Board import Board


class GameData:
    def __init__(self):
        self.board = Board()
        self.active_player = 'black'
        self.possible_moves = []
        self.winner = ''
        self.is_active_move_found = False
        self.correct_vectors = ()
