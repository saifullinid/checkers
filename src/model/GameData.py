import src.model.Board as smB
import src.service.GameService as ssGS


class GameData:
    def __init__(self, board, active_checkers, active_player, move_count, winner=-1):
        self.board = board
        self.active_checkers = active_checkers
        self.active_player = active_player
        self.move_count = move_count
        self.winner = winner

    def reset_game_data(self):
        self.board = smB.Board()
        # доработать из Service
        self.active_checkers = ssGS.search_active_checkers()
        self.active_player = 0
        self.move_count = 0
        self.winner = -1
