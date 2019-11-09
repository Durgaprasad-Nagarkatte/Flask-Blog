from flask import render_template, redirect, flash, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", form=form, title='Sign In') 

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('login')     