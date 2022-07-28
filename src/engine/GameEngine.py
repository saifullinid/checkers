import copy


class GameEngine:
    def __init__(self):
        print(f'Object from class {self.__class__.__name__} created')

    @classmethod
    def filling_possible_moves(cls, game_data, trigger=True):
        game_data.distribute_classes()

        board = game_data.board
        active_checkers = board.cells[game_data.active]
        enemy_checkers = board.cells[game_data.enemy]
        empty_checkers = board.cells[game_data.empty]

        for key, value in active_checkers.items():
            if value.rank:
                board.search_checker_ways_for_queen_type_one(key, value, enemy_checkers, empty_checkers)
            else:
                board.search_checker_ways_for_checker_type_one(key, value, enemy_checkers, empty_checkers)
        cls.writing_ways_to_possible_moves(game_data, active_checkers)

        if not game_data.possible_moves and trigger:
            for key, value in active_checkers.items():
                if value.rank:
                    board.search_checker_ways_for_queen_type_two(key, value, empty_checkers)
                else:
                    board.search_checker_ways_for_checker_type_two(key, value, empty_checkers)
            cls.writing_ways_to_possible_moves(game_data, active_checkers)

    @classmethod
    def make_move(cls, input_move, game_data):
        move = cls.check_move(input_move, game_data.possible_moves)
        if move:
            active_checkers = game_data.board.cells[game_data.active]
            empty_checkers = game_data.board.cells[game_data.empty]

            active_checker_key = tuple(move[-1][0])
            empty_key = tuple(move[-1][-1])

            active_checkers[empty_key] = active_checkers[active_checker_key]
            del active_checkers[active_checker_key]

            empty_checkers[active_checker_key] = empty_checkers[empty_key]
            del empty_checkers[empty_key]

            if 'one' in move[0]:
                enemy_checkers = game_data.board.cells[game_data.enemy]
                enemy_key = tuple(move[-1][1])
                game_data.possible_moves = {}

                empty_checkers[enemy_key] = copy.deepcopy(empty_checkers[active_checker_key])
                del enemy_checkers[enemy_key]

                cls.filling_possible_moves(game_data, False)
                if not game_data.possible_moves:
                    cls.move_pass(game_data)
            else:
                cls.move_pass(game_data)
        else:
            print('ERROR: its impossible to get here')

    @staticmethod
    def writing_ways_to_possible_moves(game_data, active_checkers):
        for key, checker in active_checkers.items():
            game_data.possible_moves.update(checker.checker_ways)
            checker.checker_ways = {}

    @staticmethod
    def check_move(input_move, possible_moves):
        for key, value in possible_moves.items():
            if input_move['start'] == list(value[0]) and input_move['end'] == value[-1]:
                move = [key, value]
                return move
        print('ERROR: incorrect input move')
        return False

    @classmethod
    def move_pass(cls, game_data):
        game_data.possible_moves = {}
        game_data.change_active_player()
        cls.filling_possible_moves(game_data)
        if not game_data.possible_moves:
            game_data.change_active_player()
            game_data.winner = game_data.active_player
