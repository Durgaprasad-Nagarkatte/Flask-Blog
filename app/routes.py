from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested from user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template("login.html", form=form, title='Sign In')      