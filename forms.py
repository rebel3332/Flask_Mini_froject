from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, InputRequired

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


class RegForm(FlaskForm):
    name = StringField('name', validators=[Length(min=3, max=20), InputRequired()])
    password = PasswordField('password', validators=[Length(min=3, max=20), InputRequired()])
    submit = SubmitField("Зарегистрировать")
