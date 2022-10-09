from flask import render_template, make_response, request, url_for, redirect, flash
from flask_cors import CORS
from flask_login import login_required, current_user, login_user, logout_user
import json

from src.app.model.Rooms import Storage
from src.app.forms.forms import LoginForm, RegistrationForm, NewRoomForm, ChoiceRoomForm, ChoiceColorForm
from src.app import app, db
from src.app.dbservice.dbservice import dbService

CORS(app)
storage = Storage()


@app.route('/')
@app.route('/index')
def index():
    title = 'CHECKERS'
    storage.logout_user_from_room(current_user)
    dbService.logout_user_from_room(current_user, db)
    if current_user.is_authenticated:
        name = current_user.username
        dbService.logout_user_from_room(current_user, db)
    else:
        name = None
    return render_template('index.html', title=title, name=name)


@app.route('/waiting_for_second_player/<roomname>', methods=['GET', 'POST'])
def waiting_for_second_player(roomname):
    amount_players = storage.get_amount_players_in_game_data(roomname)
    data = ''
    if amount_players == 2:
        storage.game_launch(roomname)
        data_dict = {"msg": "start"}
        data = json.dumps(data_dict)
    res = make_response(data, 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app.route('/rooms', methods=['GET', 'POST'])
@login_required
def rooms():
    storage.logout_user_from_room(current_user)
    dbService.logout_user_from_room(current_user, db)
    title = 'ROOMS'
    new_room_form = NewRoomForm()
    choice_room_form = ChoiceRoomForm()

    if new_room_form.validate_on_submit():
        roomname = new_room_form.new_room_name.data
        storage.create_room(roomname, db)
        dbService.add_player_to_room(current_user, roomname, db)
        return redirect(url_for('game', roomname=roomname))

    if choice_room_form.validate_on_submit():
        roomname = choice_room_form.choice_room_name.data
        dbService.add_player_to_room(current_user, roomname, db)
        return redirect(url_for('game', roomname=roomname))

    return render_template('rooms.html',
                           new_room_form=new_room_form,
                           choice_room_form=choice_room_form,
                           title=title)


@app.route('/game/<roomname>', methods=['GET', 'POST'])
@login_required
def game(roomname):
    form = ChoiceColorForm()
    amount_players = storage.get_amount_players_in_game_data(roomname)
    turned_class = ''

    if amount_players:
        current_color = storage.get_second_color(roomname)
        dbService.set_color(current_user.username, current_color, db)
        storage.add_player_to_game_data(roomname, current_color, current_user.username)
        amount_players = storage.get_amount_players_in_game_data(roomname)
        if current_color == 'black':
            turned_class = 'turned'
    else:
        if form.validate_on_submit():
            current_color = 'white' if form.submit_white.data else 'black'
            dbService.set_color(current_user.username, current_color, db)
            storage.add_player_to_game_data(roomname, current_color, current_user.username)
            amount_players = storage.get_amount_players_in_game_data(roomname)
            if current_color == 'black':
                turned_class = 'turned'

    rows = range(8)
    columns = range(8)
    white = 'cell white_cell'
    black = 'cell black_cell'
    game_service = storage.rooms[roomname]
    game_service.clear_game_data()
    game_service.search_moves()
    game_data_dto = game_service.get_game_data_dto()
    return render_template('game.html',
                           rows=rows,
                           columns=columns,
                           white=white,
                           black=black,
                           white_checkers=game_data_dto.white_list,
                           black_checkers=game_data_dto.black_list,
                           queens=game_data_dto.queen_list,
                           turned_class=turned_class,
                           form=form,
                           amount_players=amount_players)


@app.route('/start/<roomname>', methods=['GET', 'POST'])
@login_required
def do_start(roomname):
    game_service = storage.rooms[roomname]
    if request.method == 'POST':
        move = request.get_json(force=True)
        game_service.do_move(move)
        game_data = game_service.get_game_data_dto()
        game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
        res = make_response(game_data_json, 200)
        res.headers['Content-Type'] = 'application/json'
        return res

    game_data = game_service.get_game_data_dto()
    game_data_json = json.dumps(game_data, default=lambda x: x.__dict__)
    res = make_response(game_data_json, 200)
    res.headers['Content-Type'] = 'application/json'
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = dbService.login_current_user(form.username.data,
                                            form.password.data)
        if user:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('rooms'))

        flash('Invalid username or password')
        return redirect(url_for('login'))

    return render_template('login.html',
                           form=form,
                           title='LOGIN')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    storage.logout_user_from_room(current_user)
    dbService.logout_user_from_room(current_user, db)
    logout_user()
    return redirect(url_for('index'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = dbService.add_new_user(db,
                                      form.username.data,
                                      form.email.data,
                                      form.password.data)
        if not user:
            flash('This name or email is already taken')
            return redirect(url_for('registration'))
        flash('player registered')
        return redirect(url_for('login'))

    return render_template('registration.html',
                           form=form,
                           title='REGISTRATION')


@app.route('/rdel', methods=['GET', 'POST'])
def delete_rooms():
    dbService.delete_all_rooms(db)
    return redirect(url_for('index'))
