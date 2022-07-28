import model.GameData as smGD
import dto.GameDataDTO as sdGD_DTO
import engine.GameEngine as seGE


class GameService:
    def __init__(self):
        self.game_data = smGD.GameData()
        print(f'Object from class {self.__class__.__name__} created')

    def get_game_data_dto(self):
        game_data_dto = sdGD_DTO.GameDataDTO(self.game_data)
        return game_data_dto

    def search_moves(self):
        seGE.GameEngine.filling_possible_moves(self.game_data)
        game_data_dto = self.get_game_data_dto()
        return game_data_dto

    def do_move(self, input_move):
        seGE.GameEngine.make_move(input_move, self.game_data)
        game_data_dto = self.get_game_data_dto()
        return game_data_dto
