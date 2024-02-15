from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from datetime import date, datetime
from models import Comment
from forms import CommentForm
from werkzeug.utils import secure_filename

from extensions import app, db

comments = Blueprint("comments", __name__)


@comments.route('posts/<post_id>/comments/new', methods=['POST'])
@login_required
def new_post(post_id):
    """route to create a new comment on a post"""
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(
            text=form.comment.data,
            score=0,
            created_by=current_user.id,
            attached_to_id=post_id
        )

        db.session.add(new_comment)
        db.session.commit()

        flash('comment added')

    return redirect(url_for('posts.get_post', post_id=post_id))


# @comments.route('/comments', methods=['GET'])
# def all_comments():
#     all_comments = Post.query.all()
#     print(all_comments)
#     return render_template('browse.html', all_comments=all_comments)


# @comments.route('/comments/<post_id>', methods=['GET', 'POST'])
# def get_post(post_id):
#     post = Post.query.get(post_id)
#     form = PostForm(obj=post)

#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.description = form.description.data

#         try:
#             filename = secure_filename(form.media.data.filename)
#             form.file.data.save('uploads/' + filename)
#         except AttributeError:
#             filename = post.media

#         post.media = filename

#     db.session.commit()

#     return render_template('post.html', post=post, form=form)


# @comments.route('/comments/delete/<post_id>', methods=['GET'])
# def delete_post(post_id):
#     post = Post.query.filter_by(id=post_id).delete()
#     db.session.commit()

#     return redirect(url_for('comments.all_comments'))
