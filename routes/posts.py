from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from models import Post
from forms import PostForm
from werkzeug.utils import secure_filename

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

    flash('post added')

    return render_template('index.html')
  return render_template('new_post.html', form=form)