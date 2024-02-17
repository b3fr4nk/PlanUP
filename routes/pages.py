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
