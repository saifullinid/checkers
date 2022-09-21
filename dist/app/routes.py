from flask import render_template, make_response, request
from flask import Flask
from flask_cors import CORS
import os
import json
from .service.GameService import GameService


TEMPLATE_DIR = os.path.abspath('../dist/html/templates')
STATIC_DIR = os.path.abspath('../dist')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
CORS(app)

game_service = GameService()


@app.route('/')
@app.route('/index')
def index():
    title = 'CHECKERS'
    return render_template('index.html', title=title)


@app.route('/game', methods=['GET', 'POST'])
def game():
    rows = range(8)
    columns = range(8)
    white = 'cell white_cell'
    black = 'cell black_cell'
    game_data_dto = game_service.get_game_data_dto()
    return render_template('game.html',
                           rows=rows,
                           columns=columns,
                           white=white,
                           black=black,
                           white_checkers=game_data_dto.white_list,
                           black_checkers=game_data_dto.black_list,
                           queens=game_data_dto.queen_list)


@app.route('/start', methods=['GET', 'POST'])
def do_start():
    if request.method == 'POST':
        move = request.get_json(force=True)
        game_data = game_service.do_move(move)
        # print(f'!!!game_data.possible_moves!!!\n {game_data.possible_moves}')
        game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
        res = make_response(game_data_json, 200)
        res.headers['Content-Type'] = 'application/json'
        return res

    game_data = game_service.search_moves()
    # print(f'!!!game_data.possible_moves!!!\n {game_data.possible_moves}')
    game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
    res = make_response(game_data_json, 200)
    res.headers['Content-Type'] = 'application/json'
    return res
