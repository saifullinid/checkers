class Checker:
    def __init__(self, row, column, rank):
        self.row = row
        self.column = column
        self.rank = rank
        self.color = ''
        self.rays = {}

    def __repr__(self):
        return f'{self.row}:{self.column}:{self.color}'

    def set_rank(self, rank):
        self.rank = rank


class BlackChecker(Checker):
    def __init__(self, row, column, rank):
        super().__init__(row, column, rank)
        self.color = 'black'


class WhiteChecker(Checker):
    def __init__(self, row, column, rank):
        super().__init__(row, column, rank)
        self.color = 'white'
