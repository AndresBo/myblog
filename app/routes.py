from flask import render_template
from app import app

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
    
