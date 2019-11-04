from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return '<h1>Hello, World!</h1>'