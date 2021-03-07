from flask import render_template, flash, url_for, redirect, request
from app import app, db
from app.forms import LoginForm, RegisterForm
from flask_login import login_required,  current_user, login_user, logout_user
from app.models import User


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

        user = User.query.filter_by(email=form.email.data).first()
        
        if user is None or not user.check_password(form.password.data):
            
            flash('Invalid email or password')
            
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        
        next_page = request.args.get('next')
        
        if not next_page or url_parse(next_page).netloc != '':
          
            next_page = url_for('blog')
        
        return redirect(next_page)

    return render_template('login.html', title = 'Sign in', form = form)


@app.route('/blog')
@login_required
def blog():

    pitches = [
        {
            'author': { 'username' : 'John' },
            'body' : 'My new pitch'
        }
    ]

    return render_template('blog.html', pitches = pitches)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/comment')
@login_required
def comment():

    return render_template('comment.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect (url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Regestration successfull!')

        return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form = form)