class Cell:
    def __init__(self, content, x_coord, y_coord, number):
        # content: '-1' - empty; '0' - white checker; '1' - black checker
        # x_coord, y_coord - range [0:7]
        # number - if content '0' or '1' - range [0:11] for white checkers and black checkers
        self.content = content
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.number = number
        self.rank = 0
        self.active = 0

    def __repr__(self):
        return f'Cell (x_coord:y_coord):({self.x_coord}:{self.y_coord}) content:{self.content}; number:{self.number}'

    def set_content(self, content):
        self.content = content

    def set_coord(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def rank_change(self):
        self.rank = 1

    def delete_content(self):
        self.content = -1
