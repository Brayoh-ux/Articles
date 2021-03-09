from flask import render_template, flash, url_for, redirect, request
from app import app, db, bcrypt
from app.forms import LoginForm, RegisterForm, UpdateForm
from flask_login import login_required,  current_user, login_user, logout_user
from app.models import User


posts = [
    {
    'author': 'Brayoh',
    'title': 'Blog 1',
    'content': 'First Post',
    'date_posted': 'March 8, 2018'
    },
    {
    'author': 'Mirriam',
    'title': 'Blog 2',
    'content': 'First Post',
    'date_posted': 'March 8, 2020'
    }
]

@app.route('/')
def index():


    return render_template('home.html', posts = posts)

@app.route('/register', methods = ['GET', 'POST'])
def register():

   form = RegisterForm()

   if form.validate_on_submit():

       password = bcrypt.generate_password_hash( form.password.data).decode('utf-8')
       user = User(username = form.username.data, email = form.email.data, password = password)

       db.session.add(user)
       db.session.commit()


       flash('Account created, You can now log in', 'success')

       return redirect(url_for('login'))

   return render_template('register.html', title= 'Register', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember_me.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('index'))

        else:
            flash('Invalid email or password')

        # else:
        #     flash('Invalid email or password', 'danger')

        # user = User.query.filter_by(email=form.email.data).first()
        
        # if user is None or not user.check_password(form.password.data):
            
        #     flash('Invalid email or password')
            
        #     return redirect(url_for('login'))
        
        # login_user(user, remember=form.remember_me.data)
        
        # 
        
        # if not next_page or url_parse(next_page).netloc != '':
          
        #     next_page = url_for('index')
        
        # return redirect(next_page)

    return render_template('login.html', title = 'Sign in', form = form)


@app.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.emal = form.email.data
        db.session.commit()
        
        flash('Account Submited!', 'success')

        return redirect (url_for('account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename = 'profilepics/anonymous.jpeg')

    return render_template('account.html', title = 'Account', image_file = image_file, form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/comment')
@login_required
def comment():

    return render_template('comment.html')


