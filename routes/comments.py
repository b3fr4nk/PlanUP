from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from datetime import date, datetime
from models import Comment
from forms import CommentForm
from werkzeug.utils import secure_filename

from extensions import app, db

comments = Blueprint("comments", __name__)


@comments.route('/posts/<post_id>/comments/new', methods=['POST'])
@login_required
def new_comment(post_id):
    """route to create a new comment on a post"""
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(
            text=form.comment.data,
            created_by=current_user.id,
            attached_to_id=post_id
        )

        db.session.add(new_comment)
        db.session.commit()

        flash('comment added')

    return redirect(url_for('posts.get_post', post_id=post_id))
