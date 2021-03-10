from flask import render_template,abort ,flash, url_for, redirect, request
from app import app, db, bcrypt
from app.forms import PostForm ,LoginForm, RegisterForm, UpdateForm
from flask_login import login_required,  current_user, login_user, logout_user
from app.models import User, Post
import secrets, os
import requests, json


@app.route('/')
def index():

    posts = Post.query.all()

    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    
    json_resp = response.json()

    quotes = json_resp
    # print(quotes['author'] )

    return render_template('home.html', posts = posts, quotes = quotes)

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

    return render_template('login.html', title = 'Sign in', form = form)


def save_picture(form_picture):
    # rondom hex
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profilepics', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route('/account', methods = ['GET', 'POST'])
def account():
    form = UpdateForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.imgae_file = picture_file

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


@app.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():

    form = PostForm()
    if form.validate_on_submit():

        post = Post(title = form.title.data, content = form.content.data, author = current_user)

        db.session.add(post)
        db.session.commit()

        flash('Post added successfull!', 'success')
        return redirect(url_for('index'))

    return render_template('post.html',title = 'New post', form = form, legend = 'New Post' )

@app.route('/post/update/<post_id>', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        db.session.commit()

        flash('Post successfully updated', 'success')
        return redirect( url_for('index') )

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content


    return render_template('post.html',title = 'Update post', form = form , legend = 'Update Post')

@app.route('/post/delete_post/<post_id>', methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    # if post.author != current_user:
    #     abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Post deleted', 'success')
    return redirect( url_for('index'))


