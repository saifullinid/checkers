import copy


class GameDataDTO:
    def __init__(self, game_data):
        self.board = copy.deepcopy(game_data.board)
        self.change_board_cells_tuple_keys_to_str()
        self.active_player = game_data.active_player
        self.winner = game_data.winner
        self.possible_moves = game_data.possible_moves
        print(f'Object from class {self.__class__.__name__} created; Cells: {self.board.cells}')

    def change_board_cells_tuple_keys_to_str(self):
        temp_cells_dict = {}
        for type_cells, cells_dict in self.board.cells.items():
            for coord, cell in cells_dict.items():
                temp_cells_dict[str(coord)] = copy.deepcopy(cell)
            self.board.cells[type_cells] = temp_cells_dict
