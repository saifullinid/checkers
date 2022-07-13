class InputMoveDTO:
    def __init__(self, move):
        self.move = move
        print(f'Object from class {self.__class__.__name__} created')

    def __repr__(self):
        return f'Move: ({self.move})'
