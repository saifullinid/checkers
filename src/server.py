# import json
import service.GameService as ssGS
from flask import Flask
from flask import jsonify, json, make_response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

game_service = ssGS.GameService()


@app.route('/ping', methods=['GET'])
# @cross_origin()
def do_ping():
    print('ping')
    res = make_response('pong', 200)
    res.headers['Content-Type'] = 'text/plain'
    return res


@app.route('/start', methods=['GET'])
# @cross_origin()
def do_start():
    print('start')
    game_data = game_service.search_moves()
    game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
    res = make_response(game_data_json, 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app.route('/', methods=['POST'])
# @cross_origin()
def do_move():
    print('move')
    move = request.get_json(force=True)
    game_data = game_service.do_move(move)
    game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
    res = make_response(game_data_json, 200)
    res.headers['Content-Type'] = 'application/json'
    return res


if __name__ == '__main__':
    app.run()
