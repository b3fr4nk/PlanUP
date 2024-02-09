from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import User
from forms import SignupForm

from extensions import db, bcrypt

users = Blueprint('users', __name__)
auth = Blueprint('auth', __name__)

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    GET: Returns sign up page
    POST: Creates new user and redirects to all_posts
    """
    form = SignupForm()

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
    return render_template('signup.html', form=form)


@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    return render_template('user.html', user=user)


@users.route('/users/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.delete(user_id)

    db.session.commit()

    return redirect(url_for('posts.all_posts'))
