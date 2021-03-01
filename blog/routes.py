from flask import render_template,url_for,flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm


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
        flash(f'Account for {form.username.data} created!', 'success')
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
