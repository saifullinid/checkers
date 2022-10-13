from src.app.model.Board import Board


class GameData:
    def __init__(self):
        self.board = Board()
        self.active_player = 'white'
        self.players = {}
        self.possible_moves = []
        self.move = {}
        self.winner = ''
        self.is_active_move_found = False
        self.is_active_player_changed = False
        self.correct_vectors = ()
