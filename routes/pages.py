"""Temporary routes for testing frontend"""
from flask import Blueprint, render_template, redirect, url_for
from models import User
from forms import LoginForm

from extensions import db, bcrypt

pages = Blueprint('pages', __name__)

@pages.route('/')
def landing_page():
    """Return landing page"""
    return render_template('index.html')

@pages.route('/browse')
def browse_page():
    """Return browse page"""
    return render_template('browse.html')

@pages.route('/signin', methods=['GET'])
def signin():
    """
    GET: Returns sign in page
    Redirect to profile
    """
    form = LoginForm()

    if form.validate_on_submit():
        print('valid')
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('posts.all_posts'))
    return render_template('signin.html', form=form)
