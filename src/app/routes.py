from flask import render_template, make_response, request, url_for, redirect
from flask import Flask
from flask_cors import CORS
import json
from .config import Config, TEMPLATE_DIR, STATIC_DIR
from .service.GameService import GameService
from .forms.forms import LoginForm, RegistrationForm, NewRoomForm, ChoiceRoomForm

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_object(Config)
CORS(app)

game_service = GameService()


@app.route('/')
@app.route('/index')
def index():
    title = 'CHECKERS'
    return render_template('index.html', title=title)


@app.route('/rooms', methods=['GET', 'POST'])
def rooms():
    title = 'ROOMS'
    new_room_form = NewRoomForm()
    choice_room_form = ChoiceRoomForm()
    if new_room_form.validate_on_submit():
        print(f'room_name {new_room_form.new_room_name.data}')
    if choice_room_form.validate_on_submit():
        print(f'room_name {choice_room_form.choice_room_name.data}')
    return render_template('rooms.html',
                           new_room_form=new_room_form,
                           choice_room_form=choice_room_form,
                           title=title)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'username {form.username.data} '
              f'password {form.password.data} '
              f'remember_me {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',
                           form=form,
                           title='LOGIN')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(f'username {form.username.data} '
              f'password {form.password.data} '
              f'email {form.email.data}')
        return redirect(url_for('index'))
    return render_template('registration.html',
                           form=form,
                           title='LOGIN')
