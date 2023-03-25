from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'andres'}
    posts = [
        {
            'author': {'username':'John'},
            'body':'Beautiful day in Brisbane'
        },
        {
            'author': {'username':'Susana'},
            'body': 'Lets review a movie'
        },
        {
            'author': { 'username':'Andres'},
            'body':'Avengers?'
        }

    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
