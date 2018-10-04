from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Troy'},
            'body': "I give this year a 'D', for delightful!"
        },
        {
            'author': {'username': 'Abed'},
            'body': 'Six Seasons and a Movie!'
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
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)