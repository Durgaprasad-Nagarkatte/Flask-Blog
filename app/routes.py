from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    title = "Durgaprasad"
    user = {"username": "Durgaprasad"}
    posts = [
        {
            "author": "Akshatha",
            "body": "What a beautiful day. !!"
        },
        {
            "author": "Mangala",
            "body": "Having a great time in Mumbai. !!"
        }]
    print(posts)
    return render_template("index.html", user=user, title=title, posts=posts)