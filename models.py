from extensions import db
from flask_login import UserMixin


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    # Set nullable to false once authentication is implemented
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    owner = db.relationship('User')
    media = db.Column(db.Text)
    score = db.Column(db.Integer)


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer)
    created_by = db.Column(db.Integer, db.ForeignKey('User.id'))
    user_comment = db.relationship('User')
    attached_to_id = db.Column(db.Integer, db.ForeignKey('Post.id'))
    post_comment = db.relationship('Post')
