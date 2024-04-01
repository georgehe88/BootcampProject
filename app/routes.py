# app/routes.py

from app import app
from flask import render_template
from app.api import get_external_data

@app.route('/')
def home():
    return render_template('home.html', title='Home Page', page_name='home page')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/external-data')
def external_data():
    data = get_external_data()
    return render_template('external_data.html', data=data)