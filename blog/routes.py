from flask import render_template,url_for,flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
# from .models import User

post = [
    {
        'author':'Brayoh',
        'title':'Blog 1',
        'content':'First Blog Post',
        'date_posted': 'Feb 28, 20221'
    },
    {
        'author':'John Doe',
        'title':'Blog 2',
        'content':'Second Blog Post',
        'date_posted': 'Jan 28, 20221'
    }
]

@app.route('/')
def home():
    return render_template('home.html', post = post )

@app.route('/about')
def about():
    about = 'About page'
    return render_template('about.html', title = about)   


@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        usename = form.username.data
        password = form.password.data

        user_object = User.query.filter_by( usename = usename).first()
        if user_object:
            return 'Someone has taken this username!'

        user = User(usename = usename, password = password)
        db.session.add(user)
        db.session.commit()
        return 'Saved to DB!'

    flash(f'Account for {form.username.data} created succefully!', 'success')
    return redirect(url_for('home'))

        
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'brayo@gg.com' and form.password.data == '1234':
            flash('You have being loged in', 'success')
            return redirect(url_for('home'))
        
        else:
            flash('login unsuccefull! Please check username and password!!', 'danger')

    return render_template('login.html', title = 'Login', form = form)
