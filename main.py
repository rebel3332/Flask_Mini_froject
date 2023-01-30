from flask import Flask, render_template, request, redirect, url_for

from config import Config
from forms import RegForm
from logic import User

app = Flask(__name__)
app.config.from_object(Config)

# Список зарегистрированных пользователей
users = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', users=users)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        password = request.form.get('password')
        users.append(User(name, password))
        return redirect(url_for('index'))
    return render_template('reg.html', form=form)


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()
