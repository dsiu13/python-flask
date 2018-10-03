from flask import render_template
from app import app

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
