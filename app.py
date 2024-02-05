from extensions import app, db
# import routes
from routes.posts import posts

from flask import Flask, request, redirect, render_template, url_for, jsonify

app.register_blueprint(posts)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
