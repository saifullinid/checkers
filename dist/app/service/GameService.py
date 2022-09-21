from ..model.GameData import GameData
from ..dto.GameDataDTO import GameDataDTO
from ..engine.GameEngine import GameEngine


class GameService:
    def __init__(self):
        self.game_data = GameData()
        print(f'Object from class {self.__class__.__name__} created')

    def get_game_data_dto(self):
        game_data_dto = GameDataDTO(self.game_data)
        return game_data_dto

    def search_moves(self):
        GameEngine.filling_possible_moves(self.game_data)
        return self.get_game_data_dto()

    def do_move(self, input_move):
        GameEngine.make_move(input_move, self.game_data)
        return self.get_game_data_dto()
