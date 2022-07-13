import model.Cell as smCell


class Board:
    def __init__(self):
        # заполняем доску клетками
        self.cells_list = self.__class__.filling_board()
        self.room = 0
        print(f'Object from class {self.__class__.__name__} created')

    @staticmethod
    def filling_board():
        black_count = 0
        white_count = 0
        cells_list = []
        for x in range(8):
            for y in range(8):
                if (x + y)%2 == 1:
                    if 0 <= x <= 2:
                        cells_list.append(smCell.Cell(1, x, y, black_count, rank=0))
                        black_count += 1
                    elif 3 <= x <= 4:
                        cells_list.append(smCell.Cell(-1, x, y, number=-1, rank=-1))
                    else:
                        cells_list.append(smCell.Cell(0, x, y, white_count, rank=0))
                        white_count += 1
        return cells_list
