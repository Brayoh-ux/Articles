from flask import render_template
from app import app



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