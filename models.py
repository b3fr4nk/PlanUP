from extensions import db
from flask_login import UserMixin


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    # uncomment when comments are implemented
    # comments_id = db.Column(db.text, db.ForeignKey('comment.id'))
    # comments = db.relationship("Comment", back_populates="post")
    description = db.Column(db.Text)
    # uncomment when users are implemented
    # owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # owner = db.relationship('User')
    media = db.Column(db.Text)
    score = db.Column(db.Integer)
