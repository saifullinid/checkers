from .Checker import BlackChecker, WhiteChecker
from .test_filling import test_filling_board_1


class Board:
    def __init__(self):
        self.black = BlackChecker
        self.white = WhiteChecker
        self.own_class = ''
        self.enemy_class = ''
        self.field = {}
        self.ignored_vector = ()
        # test_filling_board_1(self)
        self.filling_field()

    def __repr__(self):
        output = ''
        for key, value in self.field.items():
            output = output + f'{key},{value}\n'
        return output

    def filling_field(self):
        rows = range(8)
        columns = range(8)
        for row in rows:
            for column in columns:
                if (row + column) % 2 == 1:
                    key = (row, column)
                    if 0 <= row <= 2:
                        self.field[key] = BlackChecker(row, column, 0)
                    elif 3 <= row <= 4:
                        self.field[key] = 'empty'
                    else:
                        self.field[key] = WhiteChecker(row, column, 0)

    def filling_rays(self, current_checker):
        self.clear_rays()
        if not current_checker:
            for checker in self.field.values():
                if checker != 'empty':
                    if not checker.rank:
                        self.__search_checkers_rays(checker)
                    else:
                        self.__search_queen_rays(checker)
        else:
            if not current_checker.rank:
                self.__search_checkers_rays(current_checker)
            else:
                self.__search_queen_rays(current_checker)

    def __search_checkers_rays(self, checker):
        vectors = (-1, -1), (-1, 1), (1, -1), (1, 1)
        for vector in vectors:
            ray = []
            i, j = vector
            current_coordinate = checker.row + i, checker.column + j
            if self.field.get(current_coordinate):
                ray.append(self.field[current_coordinate])
                current_coordinate = checker.row + i + i, checker.column + j + j
                if self.field.get(current_coordinate):
                    ray.append(self.field[current_coordinate])
            checker.rays[vector] = ray

    def __search_queen_rays(self, queen):
        if not self.ignored_vector:
            vectors = (-1, -1), (-1, 1), (1, -1), (1, 1)
        else:
            ignored_vector = set(self.ignored_vector)
            vectors_set = {(-1, -1), (-1, 1), (1, -1), (1, 1)} - ignored_vector
            vectors = tuple(vectors_set)

        for vector in vectors:
            ray = []
            i, j = vector
            current_coordinate = queen.row + i, queen.column + j
            while self.field.get(current_coordinate):
                ray.append(self.field[current_coordinate])
                current_coordinate = current_coordinate[0] + i, current_coordinate[1] + j
            queen.rays[vector] = ray
        self.ignored_vector = ()

    def clear_rays(self):
        for checker in self.field.values():
            if checker != 'empty':
                checker.rays = {}
