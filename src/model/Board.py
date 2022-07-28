# import model.Cell as smCell
import model.Cells as smC
# import src.model.Cells as smC


class Board:
    def __init__(self):
        # заполняем доску клетками
        self.cells = {
            'black': {},
            'white': {},
            'empty': {}
            }
        self.filling_board()
        self.room = 0
        print(f'Object from class {self.__class__.__name__} created')

    def filling_board(self):
        black_count = 0
        white_count = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    if 0 <= x <= 2:
                        self.cells['black'][(x, y)] = smC.BlackCheckerCell(black_count)
                        black_count += 1
                    elif 3 <= x <= 4:
                        self.cells['empty'][(x, y)] = smC.EmptyCell()
                    else:
                        self.cells['white'][(x, y)] = smC.WhiteCheckerCell(white_count)
                        white_count += 1
        return None

    @staticmethod
    def search_checker_ways_for_checker_type_one(key, cell, enemy_cells_dict, empty_cells_dict):
        count = 0
        for i, j in [-1, -1], [-1, 1], [1, -1], [1, 1]:
            enemy_key = (key[0] + i, key[1] + j)
            if enemy_key in enemy_cells_dict.keys():
                empty_key = (key[0] + i + i, key[1] + j + j)
                if empty_key in empty_cells_dict.keys():
                    str_key = str((key, count, 'one'))
                    cell.checker_ways[str_key] = [list(key), list(enemy_key), list(empty_key)]
                    count += 1

    @staticmethod
    def search_checker_ways_for_queen_type_one(key, cell, enemy_cells_dict, empty_cells_dict):
        count = 0
        for i, j in [-1, -1], [-1, 1], [1, -1], [1, 1]:
            enemy_key = None
            k = i
            n = j
            while True:
                current_key = (key[0] + k, key[1] + n)
                if current_key in enemy_cells_dict.keys():
                    if not enemy_key:
                        k += i
                        n += j
                        enemy_key = current_key
                    else:
                        break
                elif current_key in empty_cells_dict.keys():
                    if enemy_key:
                        str_key = str((key, count, 'one'))
                        cell.checker_ways[str_key] = [list(key), list(enemy_key), list(current_key)]
                        k += i
                        n += j
                        count += 1
                    else:
                        k += i
                        n += j
                else:
                    break

    @staticmethod
    def search_checker_ways_for_checker_type_two(key, cell, empty_cells_dict):
        count = 0
        l, m = ([-1, 1], [-1, -1]) if 'WhiteCheckerCell' in str(type(cell)) else ([1, 1], [1, -1])
        for i, j in l, m:
            empty_key = (key[0] + i, key[1] + j)
            if empty_key in empty_cells_dict.keys():
                str_key = str((key, count, 'two'))
                cell.checker_ways[str_key] = [list(key), list(empty_key)]
                count += 1

    @staticmethod
    def search_checker_ways_for_queen_type_two(key, cell, empty_cells_dict):
        count = 0
        for i, j in [-1, -1], [-1, 1], [1, -1], [1, 1]:
            k = i
            n = j
            while True:
                current_key = (key[0] + k, key[1] + n)
                if current_key in empty_cells_dict.keys():
                    str_key = str((key, count, 'two'))
                    cell.checker_ways[str_key] = [list(key), list(current_key)]
                    k += i
                    n += j
                    count += 1
                else:
                    count += 1
                    break
