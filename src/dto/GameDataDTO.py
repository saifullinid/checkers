class GameDataDTO:
    def __init__(self, game_data):
        self.board = game_data.board
        self.active_checkers = game_data.active_checkers
        self.active_player = game_data.active_player
        self.move_count = game_data.move_count
        self.winner = game_data.winner
        self.possible_moves = game_data.possible_moves
        print(f'Object from class {self.__class__.__name__} created')
