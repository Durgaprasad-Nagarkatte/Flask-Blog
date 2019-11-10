from flask import render_template, redirect, flash, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered with our site.')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)
    
@app.route('/user/<username>')
@login_required
def user(username):
    #if not current_user.is_authenticated:
    #    return redirect(url_for('login'))
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Profile updated')
        redirect(url_for('edit_profile'))

    if request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template("edit_profile.html", form=form, title="Edit Profile")

