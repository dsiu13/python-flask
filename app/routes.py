from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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
            'body': 'Six Seasons and a Movie'
        },
        {
            'author': {'username': 'Jeff'},
            'body': 'Doing more than the minimum amount of work is my definition of failing.'
        },
        {
            'author': {'username': 'Annie'},
            'body': 'That was a game. This is paintball.'
        },
        {
            'author': {'username': 'Britta'},
            'body': "The perfect Jeff Winger blow-off class: a class that doesn't exist."
        },
        {
            'author': {'username': 'Shirley'},
            'body': "Kind people are always kind, not just when it's easy."
        },
        {
            'author': {'username': 'Pierce'},
            'body': "When we seek to destroy others, we often hurt ourselves, because it's the self that wants to be destroyed."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
