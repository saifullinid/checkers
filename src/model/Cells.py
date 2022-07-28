class CellsPropValue:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Cells:
    rank = CellsPropValue()
    checker_ways = CellsPropValue()

    def __init__(self, number, rank):
        self.checker_ways = {}
        self.number = number
        self.rank = rank
        # print(f'Object from class {self.__class__.__name__} created')

    def __repr__(self):
        return f'{self.__class__.__name__} number:{self.number}; rank:{self.rank}'


class EmptyCell(Cells):
    def __init__(self):
        super().__init__(-1, -1)


class WhiteCheckerCell(Cells):
    def __init__(self, number):
        super().__init__(number, 0)


class BlackCheckerCell(Cells):
    def __init__(self, number):
        super().__init__(number, 0)
