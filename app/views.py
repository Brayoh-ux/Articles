from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
def index():

    user = {'username' : 'Brian'}

    pitches = [
        {
            'author': { 'username' : 'John' },
            'body' : 'My first pitch'
        }
    ]

    return render_template('home.html', user = user, pitches = pitches)


@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        flash('Login Succefull!')
        return redirect( url_for('index'))

    return render_template('login.html', title = 'Sign in', form = form)