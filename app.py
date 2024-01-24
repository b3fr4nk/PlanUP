from extensions import app, db
# import routes

from flask import Flask, request, redirect, render_template, url_for, jsonify

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)