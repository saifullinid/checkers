class Room:
    cls_counter = 0

    def __init__(self):
        self.__class__.cls_counter += 1
        self.number = self.__class__.cls_counter

    def __del__(self):
        print(f'Room number:{self.number} destroyed')
