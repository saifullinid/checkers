from src.app.model.GameData import GameData
from src.app.dto.GameDataDTO import GameDataDTO
from src.app.engine.GameEngine import GameEngine


class GameService:
    def __init__(self):
        self.game_data = GameData()
        self.game_data_dto = None

    def set_game_data_dto(self):
        self.game_data_dto = GameDataDTO(self.game_data)
        return self.game_data_dto

    def get_game_data_dto(self):
        self.set_game_data_dto()
        return self.game_data_dto

    def search_moves(self):
        GameEngine.filling_possible_moves(self.game_data)
        return self.get_game_data_dto()

    def do_move(self, input_move):
        GameEngine.make_move(input_move, self.game_data)
        return self.get_game_data_dto()
