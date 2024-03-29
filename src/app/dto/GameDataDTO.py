class GameDataDTO:
    def __init__(self, game_data):
        self.active_player = game_data.active_player
        self.winner = game_data.winner
        self.possible_moves = game_data.possible_moves
        self.players = game_data.players
        self.move = game_data.move
        self.is_active_player_changed = game_data.is_active_player_changed
        self.black_list = []
        self.white_list = []
        self.queen_list = []
        self.create_field_lists(game_data)
        self.check_players_and_set_winner()

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

    def check_players_and_set_winner(self):
        if len(self.players.keys()) < 2:
            if self.players.get('white'):
                self.winner = 'white'
            else:
                self.winner = 'black'
