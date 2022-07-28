import model.Board as smB


class GameData:
    def __init__(self):
        self.board = smB.Board()
        self.active_player = 0
        self.active = None
        self.enemy = None
        self.empty = 'empty'
        self.winner = -1
        self.possible_moves = {}
        self.distribute_classes()
        print(f'Object from class {self.__class__.__name__} created')

    def change_active_player(self):
        if self.active_player:
            self.active_player = 0
            self.distribute_classes()
        else:
            self.active_player = 1
            self.distribute_classes()

    def distribute_classes(self):
        if self.active_player == 0:
            self.active = 'white'
            self.enemy = 'black'
        else:
            self.active = 'black'
            self.enemy = 'white'


# gd = GameData()
# print(gd.board.cells[gd.active])
