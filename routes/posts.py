from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from models import Post
from forms import PostForm
from werkzeug.utils import secure_filename

from extensions import app, db

posts = Blueprint("posts", __name__)

@posts.route('/posts/new', methods=['GET', 'POST'])
def new_post():
  form = PostForm()

  if form.validate_on_submit():
    print('valid')
    filename = ''
    if form.media.data is not None:
      filename = secure_filename(form.media.data.filename)
      form.file.data.save('uploads/' + filename)
    
    new_post = Post(
      title = form.title.data,
      description = form.description.data,
      media = f'uploads/{filename}',
      score = 0
      #TODO add comments and owner when they are implemented
    )

    db.session.add(new_post)
    db.session.commit()

    flash('post added')

    return redirect(url_for('posts.all_posts'))
  return render_template('new_post.html', form=form)

@posts.route('/posts', methods=['GET'])
def all_posts():
  all_posts = Post.query.all()
  print(all_posts)
  return render_template('browse.html', all_posts=all_posts)

@posts.route('/posts/<post_id>', methods=['GET', 'POST'])
def get_post(post_id):
  post = Post.query.get(post_id)
  form = PostForm(obj=post)

  if form.validate_on_submit():
    post.title = form.title.data
    post.description = form.description.data

    # TODO find a way to update the file without throwing an error when there is no update
    # try:

    #   if form.media.data is not None:
    #     filename = secure_filename(form.media.data.filename)
    #     form.file.data.save('uploads/' + filename)
    #     post.media = filename
    # except:
    #   print('invalid file type')
  db.session.commit()

  return render_template('post.html', post=post, form=form)

@posts.route('/posts/delete/<post_id>', methods=['GET'])
def delete_post(post_id):
  post = Post.query.filter_by(id=post_id).delete()
  db.session.commit()

  return redirect(url_for('posts.all_posts'))

