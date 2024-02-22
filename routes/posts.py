from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from models import Post
from forms import PostForm
from werkzeug.utils import secure_filename

from extensions import app, db

posts = Blueprint("posts", __name__)


@posts.route('/posts/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        print('valid')
        try:
            filename = secure_filename(form.media.data.filename)
            form.file.data.save('uploads/' + filename)
        except AttributeError:
            filename = ''

        new_post = Post(
            title=form.title.data,
            description=form.description.data,
            media=f'uploads/{filename}',
            score=0,
            owner_id=current_user.id
        )

        db.session.add(new_post)
        db.session.commit()

        flash('post added')

        return redirect(url_for('posts.all_posts'))
    return render_template('new_post.html', form=form)


@posts.route('/posts', methods=['GET'])
def all_posts():
    all_posts = Post.query.all()
    return render_template('browse.html', all_posts=all_posts)


@posts.route('/posts/<post_id>', methods=['GET', 'POST'])
def get_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data

        try:
            filename = secure_filename(form.media.data.filename)
            form.file.data.save('uploads/' + filename)
        except AttributeError:
            filename = post.media

        post.media = filename

    db.session.commit()

    return render_template('post.html', post=post, form=form)


@posts.route('/posts/delete/<post_id>', methods=['GET'])
@login_required
def delete_post(post_id):

    post = Post.query.get(post_id)

    if post.owner_id == current_user.id:
        db.session.delete(post_id)
        db.session.commit()
    else:
        flash('you are not authorized to delete this')

    return redirect(url_for('posts.all_posts'))
