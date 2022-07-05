import src.service.GameService as ssGS


class Board:
    def __init__(self):
        # заполняем доску клетками
        self.cell_list = ssGS.filling_board()
        # доработать class Rooms
        self.room = 0
