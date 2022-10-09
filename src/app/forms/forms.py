from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, length, Email, EqualTo
from src.app.dbservice.dbservice import dbService


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    password_rep = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class NewRoomForm(FlaskForm):
    new_room_name = StringField('Create room', validators=[DataRequired(), length(min=3, max=20)])
    submit = SubmitField('Create')


class ChoiceRoomForm(FlaskForm):
    choice_room_name = SelectField('Choice room')
    submit = SubmitField('Choice')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choice_room_name.choices = dbService.get_all_roomnames()


class ChoiceColorForm(FlaskForm):
    hidden = HiddenField('hidden', default='color', validators=[DataRequired()])
    white = SubmitField('white')
    black = SubmitField('black')
