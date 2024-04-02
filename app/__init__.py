import os
from flask import Flask, render_template, request, redirect, url_for
from app.api import get_external_data
import pyrebase
import requests
import json

firebase_config = {
    "apiKey": os.environ["FIREBASE_API_KEY"],
    "authDomain": "weatherwiz-ae39f.firebaseapp.com",
    "projectId": "weatherwiz-ae39f",
    "storageBucket": "weatherwiz-ae39f.appspot.com",
    "messagingSenderId": "338475646046",
    "appId": "1:338475646046:web:15dc2d0a9bdbd76881c8cf",
    "measurementId": "G-963EZS43G1",
    "databaseURL": ""
}

app = Flask(__name__)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/external-data')
def external_data():
    data = get_external_data()
    return render_template('external_data.html', data=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_password']
        try:
            registered_user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(registered_user['idToken'])
            # Redirect to the login page after successful registration
            return redirect(url_for('login'))
        except requests.exceptions.HTTPError as exp:
            error_json = exp.args[1]
            error = json.loads(error_json)['error']
            error_message = error['message']
    return render_template('register.html', error_message=error_message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_password']
        try:
            user_info = auth.sign_in_with_email_and_password(email, password)
            account_info = auth.get_account_info(user_info['idToken'])
            print(json.dumps(account_info, indent=4))
            if account_info['users'][0]['emailVerified']:
                # Redirect to home or dashboard page after successful login
                return redirect(url_for('home'))
            return render_template('login.html', error_message='Please verify email')
        except requests.exceptions.HTTPError as exp:
            error_json = exp.args[1]
            error = json.loads(error_json)['error']
            login_error = error['message']
            return render_template('login.html', error_message=login_error)
    return render_template('login.html')
