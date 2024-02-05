"""Landing page/browse page/signup and signin page routes"""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from forms import PostForm
from extensions import app, db

pages = Blueprint("pages", __name__)

# ---------------------
# Landing page route
@pages.route('/')
def landing_page():
    """Landing page/index.html"""
    return render_template('index.html')

# ---------------------
# Browse route
@pages.route('/browse')
def browse_page():
    """Return browse.html"""
    return render_template('browse.html')

# ---------------------
# Sign In/Login route
@pages.route('/login')
def signin_page():
    """Return signin.html"""
    return render_template('signin.html')

# ---------------------
# Sign Up route
@pages.route('/signup')
def signup_page():
    """Return signup.html"""
    return render_template('signup.html')
