from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, InputRequired
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

# Список зарегистрированных пользвоателей
users=[]

class user():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        print(f'Зарегистрирован новый пользователь {self.name}')

class RegForm(FlaskForm):
    name = StringField('name',validators=[Length(min=3,max=20),InputRequired()])
    password = PasswordField('password',validators=[Length(min=3,max=20),InputRequired()])
    submit = SubmitField("Зарегистрировать")

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html',users=users)

@app.route('/reg', methods=['GET','POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        password = request.form.get('password')
        users.append(user(name,password))
        return redirect(url_for('index'))
    return render_template('reg.html', form=form)

def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()



