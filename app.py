from extensions import app, db
# import routes
from routes.posts import posts
from routes.pages import pages
from routes.users import users, auth
from routes.comments import comments

from flask import Flask, request, redirect, render_template, url_for, jsonify

app.register_blueprint(posts)
app.register_blueprint(users)
app.register_blueprint(pages)
app.register_blueprint(auth)
app.register_blueprint(comments)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
