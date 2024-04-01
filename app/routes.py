from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html', title='Home Page', page_name='home page')


@app.route('/about')
def about():
    return render_template('about.html')
