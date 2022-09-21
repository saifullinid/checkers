class GameEngine:
    @classmethod
    def filling_possible_moves(cls, game_data):
        game_data.is_active_move_found = False
        game_data.possible_moves = []
        game_data.board.filling_rays(False)

        field = game_data.board.field
        cls.definition_own_and_enemy_classes(game_data)
        own_class, enemy_class = game_data.own_class, game_data.enemy_class
        game_data.correct_vectors = cls.definition_correct_vectors(game_data)

        checker_moves = {
            'active': [],
            'passive': []
        }
        for coordinate, checker in field.items():
            if isinstance(checker, own_class):
                active_moves = cls.search_active_moves(checker, enemy_class, game_data)
                if active_moves:
                    checker_moves['active'].extend(active_moves)
                else:
                    passive_moves = cls.search_passive_moves(checker, game_data)
                    if passive_moves:
                        checker_moves['passive'].extend(passive_moves)

        if game_data.is_active_move_found:
            game_data.possible_moves = checker_moves['active']
        else:
            game_data.possible_moves = checker_moves['passive']

    @classmethod
    def search_active_moves(cls, checker, enemy_class, game_data):
        if checker.rank:
            active_moves = cls.search_queen_active_moves(checker, enemy_class)
        else:
            active_moves = cls.search_checker_active_moves(checker, enemy_class)
        if active_moves:
            game_data.is_active_move_found = True
        return active_moves

    @classmethod
    def search_passive_moves(cls, checker, game_data):
        if checker.rank:
            passive_moves = cls.search_queen_passive_moves(checker)
        else:
            passive_moves = cls.search_checker_passive_moves(checker, game_data)
        return passive_moves

    @staticmethod
    def definition_own_and_enemy_classes(game_data):
        if game_data.active_player == 'white':
            game_data.own_class, game_data.enemy_class = game_data.board.white, game_data.board.black
        else:
            game_data.own_class, game_data.enemy_class = game_data.board.black, game_data.board.white

    @staticmethod
    def definition_correct_vectors(game_data):
        if game_data.active_player == 'white':
            return (-1, 1), (-1, -1)
        else:
            return (1, 1), (1, -1)

    @staticmethod
    def search_checker_active_moves(checker, enemy_class):
        active_moves = []
        for vector, ray in checker.rays.items():
            if len(ray) == 2:
                if isinstance(ray[0], enemy_class) and ray[1] == 'empty':
                    checker_coordinate = [checker.row, checker.column]
                    enemy_coordinate = [ray[0].row, ray[0].column]
                    empty_coordinate = [enemy_coordinate[0] + vector[0], enemy_coordinate[1] + vector[1]]

                    active_moves.append([checker_coordinate, empty_coordinate, enemy_coordinate])
        # print(f'!!!IN search_checker_active_moves!!! {active_moves}')
        return active_moves

    @staticmethod
    def search_checker_passive_moves(checker, game_data):
        passive_moves = []
        correct_vectors = game_data.correct_vectors

        for vector, ray in checker.rays.items():
            if vector in correct_vectors and len(ray) != 0:
                if ray[0] == 'empty':
                    checker_coordinate = [checker.row, checker.column]
                    empty_coordinate = [checker_coordinate[0] + vector[0], checker_coordinate[1] + vector[1]]
                    enemy_coordinate = []

                    passive_moves.append([checker_coordinate, empty_coordinate, enemy_coordinate])
        return passive_moves

    @staticmethod
    def search_queen_active_moves(queen, enemy_class):
        active_moves = []
        for vector, ray in queen.rays.items():
            is_enemy_found = False
            is_search_finish = False
            i = 0
            while not is_search_finish and i < len(ray):
                item = ray[i]
                if item == 'empty' and not is_enemy_found:
                    i += 1
                    continue
                elif isinstance(item, enemy_class) and not is_enemy_found:
                    is_enemy_found = True
                    enemy_checker = item

                    j = i + 1
                    while j < len(ray):
                        item = ray[j]
                        if item == 'empty':
                            queen_coordinate = [queen.row, queen.column]
                            enemy_coordinate = [enemy_checker.row, enemy_checker.column]
                            empty_coordinate = [queen.row + vector[0] * (j + 1), queen.column + vector[1] * (j + 1)]

                            active_moves.append([queen_coordinate, empty_coordinate, enemy_coordinate])
                            j += 1
                        else:
                            is_search_finish = True
                            break
                else:
                    break
        return active_moves

    @staticmethod
    def search_queen_passive_moves(queen):
        passive_moves = []
        for vector, ray in queen.rays.items():
            i = 0
            while i < len(ray):
                item = ray[i]
                if item == 'empty':
                    queen_coordinate = [queen.row, queen.column]
                    empty_coordinate = [queen.row + vector[0] * (i + 1), queen.column + vector[1] * (i + 1)]
                    enemy_coordinate = []

                    passive_moves.append([queen_coordinate, empty_coordinate, enemy_coordinate])
                    i += 1
                else:
                    break
        return passive_moves

    @classmethod
    def make_move(cls, move, game_data):
        if cls.check_move(move, game_data):
            old_coordinate = tuple(move[0])
            new_coordinate = tuple(move[1])
            game_data.board.field[new_coordinate] = game_data.board.field[old_coordinate]
            game_data.board.field[old_coordinate] = 'empty'
            checker = game_data.board.field[new_coordinate]
            checker.row, checker.column = new_coordinate[0], new_coordinate[1]
            cls.check_coordinate_and_change_rank(checker, game_data)

            if move[-1]:
                # print(f'!!!deleted found!!!')
                ignored_vector_x = 1 if (new_coordinate[0] - old_coordinate[0]) < 0 else -1
                ignored_vector_y = 1 if (new_coordinate[1] - old_coordinate[1]) < 0 else -1
                game_data.ignored_vector = (ignored_vector_x, ignored_vector_y)

                deleted_coordinate = tuple(move[-1])
                game_data.board.field[deleted_coordinate] = 'empty'

                cls.repeat_search_for_moves(checker, game_data)
                if not game_data.is_active_move_found:
                    winner = game_data.active_player
                    cls.change_active_player(game_data)
                    cls.filling_possible_moves(game_data)
                    if not game_data.possible_moves:
                        game_data.winner = winner
                        # print(f'!!!WINNER!!! {winner}')
            else:
                winner = game_data.active_player
                cls.change_active_player(game_data)
                cls.filling_possible_moves(game_data)
                if not game_data.possible_moves:
                    game_data.winner = winner
                    print(f'!!!WINNER!!! {winner}')

    @classmethod
    def repeat_search_for_moves(cls, checker, game_data):
        game_data.is_active_move_found = False
        game_data.board.filling_rays(checker)
        active_moves = cls.search_active_moves(checker, game_data.enemy_class, game_data)
        game_data.possible_moves = active_moves
        # print(f'!!!IN repeat_search_for_moves!!!\n{game_data.possible_moves}\n')

    @staticmethod
    def check_move(move, game_data):
        if move in game_data.possible_moves:
            # print(f'!!!move found!!!')
            return True
        else:
            print(f'!!!move NOT found!!!')

    @staticmethod
    def check_coordinate_and_change_rank(checker, game_data):
        if isinstance(checker, game_data.board.white) and checker.row == 0:
            checker.rank = 1
        elif isinstance(checker, game_data.board.black) and checker.row == 7:
            checker.rank = 1

    @staticmethod
    def change_active_player(game_data):
        if game_data.active_player == 'white':
            game_data.active_player = 'black'
        else:
            game_data.active_player = 'white'
