from flask import render_template
from app import app
from app.forms import LoginForms

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Derek'}
    posts = [
        {
        'author': {'username': 'Troy'},
        'body': "I give this year a 'D', for delightful!"
        },
        {
        'author': {'username': 'Abed'},
        'body': "Six seasons and a movie"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
