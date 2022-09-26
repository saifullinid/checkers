from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, Email, EqualTo


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
    choice_room_name = SelectField('Choice room', choices=[('1fdfsdfsd', 'one'), ('2', 'two'), ('3', 'three'), ('1', 'one'), ('2', 'two'), ('3', 'three'), ('1', 'one'), ('2', 'two'), ('3', 'three'), ('1', 'one'), ('2', 'two'), ('3', 'three')])
    submit = SubmitField('Choice')
