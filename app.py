# import modules
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# flask instance
app = Flask(__name__)

# import data from database
Articles = Articles()

# routing views
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id = id)

# form validation
class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1, max=50)])
    userName = StringField('Username', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')

    ])
    confirm = PasswordField('Confirm Password')

# run
if __name__ == '__main__':
    app.run(debug=True)