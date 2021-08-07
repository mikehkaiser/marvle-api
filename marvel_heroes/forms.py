from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    name = StringField('NAME', validators=[DataRequired()])
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    confirm = PasswordField('CONFIRM PASSWORD', validators=[DataRequired(), EqualTo('password', message='REENTER PASSWORD')])
    submit_button = SubmitField()