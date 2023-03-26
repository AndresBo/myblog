from flask import render_template, flash, redirect, url_for
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if all fields validate 
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))

        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)
