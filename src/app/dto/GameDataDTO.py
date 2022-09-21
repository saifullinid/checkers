class GameDataDTO:
    def __init__(self, game_data):
        self.active_player = game_data.active_player
        self.winner = game_data.winner
        self.possible_moves = game_data.possible_moves
        self.black_list = []
        self.white_list = []
        self.queen_list = []
        self.create_field_lists(game_data)

    def create_field_lists(self, game_data):
        for coordinate, item in game_data.board.field.items():
            if isinstance(item, game_data.board.black):
                self.black_list.append(list(coordinate))
                if item.rank:
                    self.queen_list.append(list(coordinate))
            elif isinstance(item, game_data.board.white):
                self.white_list.append(list(coordinate))
                if item.rank:
                    self.queen_list.append(list(coordinate))
