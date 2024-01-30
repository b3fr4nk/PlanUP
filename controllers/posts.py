from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from models import Post
from forms import PostForm

posts = Blueprint("posts", __name__)

@posts.route('/posts/new')
def newPost():
  form = PostForm()

  if form.validate_on_submit():
    filename = secure_filename(form.file.data.filename)
    form.file.data.save('uploads/' + filename)
    
    new_post = Post(
      title = form.title.data,
      description = form.description.data,
      media = f'uploads/{filename}',
      score = 0
      #TODO add comments and owner when they are implemented
    )