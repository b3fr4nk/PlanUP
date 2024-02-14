"""Temporary routes for testing frontend"""
from flask import Blueprint, render_template, redirect, url_for
from forms import LoginForm

pages = Blueprint('pages', __name__)

@pages.route('/')
def landing_page():
    """Return landing page"""
    return render_template('index.html')

@pages.route('/browse')
def browse_page():
    """Return browse page"""
    return render_template('browse.html')

@pages.route('/signin')
def signin():
    """
    GET: Returns sign in page
    Redirect to profile
    """
    form = LoginForm()

    if form.validate_username and form.validate_password:
        print('valid')
        # Temp redirect route
        return redirect(url_for('posts.all_posts'))
    return render_template('signin.html', form=form)
