# import src.model.GameData as GD
class GameEngine:
    def __init__(self):
        print(f'Object from class {self.__class__.__name__} created')

    @staticmethod
    def separation_cell_list(game_data):
        enemy_cells = []
        empty_cells = []
        for cell in game_data.board.cells_list:
            if cell.content == game_data.active_player:
                continue
            elif cell.content == -1:
                empty_cells.append(cell)
            else:
                enemy_cells.append(cell)
        cells = (enemy_cells, empty_cells)
        return cells

    @staticmethod
    def search_couple_for_queen(cell, empty_cells, game_data):
        count = 0
        for i, j in [1, 1], [1, -1], [-1, 1], [-1, -1]:
            k = i
            n = j
            while True:
                desired_empty_cell = next((empty_cell for empty_cell in empty_cells if (cell.x_coord + k) == empty_cell.x_coord and (cell.y_coord + n) == empty_cell.y_coord), 0)
                if not desired_empty_cell:
                    break
                key = str(cell.number) + str(count)
                game_data.possible_moves[key] = [[cell.x_coord, cell.y_coord], [], [desired_empty_cell.x_coord, desired_empty_cell.y_coord]]
                count += 1
                k += i
                n += j
        return None

    @staticmethod
    def search_couple_for_checker(cell, empty_cells, game_data):
        count = 0
        l, m = ([1, 1], [1, -1]) if game_data.active_player else ([-1, 1], [-1, -1])
        for i, j in l, m:
            desired_empty_cell = next((empty_cell for empty_cell in empty_cells if (cell.x_coord + i) == empty_cell.x_coord and (cell.y_coord + j) == empty_cell.y_coord), 0)
            if desired_empty_cell:
                key = str(cell.number) + str(count)
                game_data.possible_moves[key] = [[cell.x_coord, cell.y_coord], [], [desired_empty_cell.x_coord, desired_empty_cell.y_coord]]
                count += 1
        return None

    @staticmethod
    def search_threes_for_checker(cell, enemy_cells, empty_cells, game_data):
        count = 0
        for i, j in [-1, -1], [-1, 1], [1, -1], [1, 1]:
            while True:
                desired_enemy_cell = next((enemy_cell for enemy_cell in enemy_cells if (cell.x_coord + i) == enemy_cell.x_coord and (cell.y_coord + j) == enemy_cell.y_coord), 0)
                if desired_enemy_cell:
                    desired_empty_cell = next((empty_cell for empty_cell in empty_cells if (cell.x_coord + i + i) == empty_cell.x_coord and (
                                                           cell.y_coord + j + j) == empty_cell.y_coord), 0)
                    if desired_empty_cell:
                        key = str(cell.number) + str(count)
                        game_data.possible_moves[key] = [[cell.x_coord, cell.y_coord], [desired_enemy_cell.x_coord, desired_enemy_cell.y_coord], [desired_empty_cell.x_coord, desired_empty_cell.y_coord]]
                        count += 1
                    else:
                        break
                else:
                    break
        return None

    @staticmethod
    def search_threes_for_queen(cell, enemy_cells, empty_cells, game_data):
        def cell_list_to_possible_moves(current_list):
            start = 0
            stop = len(current_list)
            enemy_count = 0
            for number, value in enumerate(current_list):
                if value in enemy_cells:
                    if enemy_count == 0:
                        start = number
                        enemy_count = 1
                    elif enemy_count == 1:
                        stop = number
                        break
            current_list = current_list[start, stop] if (stop - start) > 1 else None
            return None

        count = 0
        cell_list = []
        for i, j in [1, 1], [1, -1], [-1, 1], [-1, -1]:
            k = i
            n = j
            while True:
                desired_enemy_cell = next((enemy_cell for enemy_cell in enemy_cells if (cell.x_coord + k) == enemy_cell.x_coord and (cell.y_coord + n) == enemy_cell.y_coord), 0)
                desired_empty_cell = next((empty_cell for empty_cell in empty_cells if (cell.x_coord + k) == empty_cell.x_coord and (cell.y_coord + n) == empty_cell.y_coord), 0)
                if desired_enemy_cell:
                    cell_list.append(desired_enemy_cell)
                    k += i
                    n += j
                elif desired_empty_cell:
                    cell_list.append(desired_empty_cell)
                    k += i
                    n += j
                else:
                    break
            cell_list_to_possible_moves(cell_list)

            if cell_list:
                desired_enemy_cell = cell_list[0]
                for num, cell_item in enumerate(cell_list):
                    if num > 0:
                        key = str(cell.number) + str(count)
                        game_data.possible_moves[key] = [[cell.x_coord, cell.y_coord], [desired_enemy_cell.x_coord, desired_enemy_cell.y_coord], [cell_item.x_coord, cell_item.y_coord]]
                        count += 1
        return None

    def search_couple(self, game_data):
        empty_cells = self.separation_cell_list(game_data)[1]
        for cell in game_data.board.cells_list:
            if cell.content == game_data.active_player:
                if cell.rank:
                    self.search_couple_for_queen(cell, empty_cells, game_data)
                else:
                    self.search_couple_for_checker(cell, empty_cells, game_data)
        return None

    def search_threes(self, game_data):
        enemy_cells = self.separation_cell_list(game_data)[0]
        empty_cells = self.separation_cell_list(game_data)[1]

        for cell in game_data.board.cells_list:
            if cell.content == game_data.active_player:
                if cell.rank:
                    self.search_threes_for_queen(cell, enemy_cells, empty_cells, game_data)
                else:
                    self.search_threes_for_checker(cell, enemy_cells, empty_cells, game_data)
        return None

    def search_possible_moves(self, game_data):
        self.search_threes(game_data)
        if not game_data.possible_moves:
            self.search_couple(game_data)
        return None

    @staticmethod
    def make_move(move, game_data):
        checker_content = -1
        checker_number = -1
        checker_rank = -1
        for cell in game_data.board.cells_list:
            if [cell.x_coord, cell.y_coord] == move[0]:
                checker_content = cell.content
                checker_number = cell.number
                checker_rank = cell.rank
                cell.content = -1
                cell.number = -1
                cell.rank = -1
            if [cell.x_coord, cell.y_coord] == move[1]:
                cell.content = -1
                cell.number = -1
                cell.rank = -1
        for cell in game_data.board.cells_list:
            if [cell.x_coord, cell.y_coord] == move[-1]:
                cell.content = checker_content
                cell.number = checker_number
                cell.rank = checker_rank
        return game_data




# gd = GD.GameData()
# s = SearchActiveCheckersEngine()
# s.search_moves(gd)
# for item in gd.board.cells_list:
#     if item.active == 1:
#         print(item.x_coord, item.y_coord)
