from src.app.service.GameService import GameService
from src.app.dbservice.dbservice import dbService


# класс-хранилище комнат
class Storage:
    def __init__(self):
        self.rooms = {}

    def __repr__(self):
        output = ''
        for roomname, service in self.rooms.items():
            output += f'{roomname} - {service} \n'
        return output

    def create_room(self, roomname):
        self.rooms[roomname] = GameService()

    def add_player_to_game_data(self, roomname, color, username):
        self.rooms[roomname].game_data.players[color] = username

    def get_second_color(self, roomname):
        if self.rooms[roomname].game_data.players.get('white'):
            return 'black'
        return 'white'

    def get_amount_players_in_game_data(self, roomname):
        return len(self.rooms[roomname].game_data.players.keys())

    def game_launch(self, roomname):
        self.rooms[roomname].search_moves()

    def logout_user_from_room(self, user):
        found_key = ''
        roomname = dbService.get_roomname_by_user(user)
        if roomname and self.rooms.get(roomname):
            for key, name in self.rooms[roomname].game_data.players.items():
                if name == user.username:
                    found_key = key
            if found_key:
                self.rooms[roomname].game_data.players.pop(found_key)
