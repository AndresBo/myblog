from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'andres'}
    return '''
    <html>
        <head>
            <title>myblog</title>
        </head>
        <body>
            <h1>Hola amigo, ''' + user['username'] + '''</h1>
        </body>
    </html>
    '''
