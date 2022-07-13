import model.GameData as smGD
import dto.GameDataDTO as sdGD_DTO
import dto.InputMoveDTO as sdIM_DTO
import engine.GameEngine as seGE


class GameService:
    def __init__(self):
        self.game_data = smGD.GameData()
        self.input_move = []
        print(f'Object from class {self.__class__.__name__} created')

    def get_game_data_dto(self):
        game_data_dto = sdGD_DTO.GameDataDTO(self.game_data)
        return game_data_dto

    def search_moves(self):
        game_data_dto = self.get_game_data_dto()
        seGE.GameEngine().search_possible_moves(game_data_dto)
        return game_data_dto

    def set_input_move(self, input_move):
        for key, value in self.game_data.possible_moves.items():
            if input_move[0] == value[0] and input_move[-1] == value[-1]:
                self.input_move = value
        return None

    def do_move(self, input_move):
        input_move_list = []
        game_data_dto = self.get_game_data_dto()
        for value in input_move.values():
            input_move_list.append(value)
        self.set_input_move(input_move_list)
        input_move_dto = sdIM_DTO.InputMoveDTO(self.input_move) if self.input_move else None
        self.game_data = seGE.GameEngine().make_move(input_move_dto.move, game_data_dto)
        return None
