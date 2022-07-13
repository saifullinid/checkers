import model.Board as smB


class GameData:
    def __init__(self):
        self.board = smB.Board()
        self.active_checkers = []
        self.active_player = 0
        self.move_count = 0
        self.winner = -1
        self.possible_moves = {}
        print(f'Object from class {self.__class__.__name__} created')
