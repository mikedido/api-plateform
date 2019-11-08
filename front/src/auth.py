# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
import requests, re

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #parse the result of the API call
    request_user = requests.get('http://localhost:9000/api/users?email='+email+'&password='+password)
    result = request_user.json()
    user_api = result['hydra:member']

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if len(user_api) == 0: 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    #login_user(user, remember=remember)
    session['loggedin'] = True
    session['id'] = user_api[0]['id']
    session['username'] = user_api[0]['lastName']
    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    #check email
    pattern_email = re.compile("^[^\W][a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*\@[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*\.[a-zA-Z]{2,4}$")
    if not pattern_email.match(email):
        flash('Email invalide')
        return redirect(url_for('auth.signup'))

    #check passwords
    pattern_password = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if not pattern_password.match(password1) :
        flash('le mot de passe doit contenir une lettre majuscule ....')
        return redirect(url_for('auth.signup'))

    if password1 != password2:
        flash('Les mots de passes doivent être identique')
        return redirect(url_for('auth.signup'))

    request_user = requests.get('http://localhost:9000/api/users?email='+email)
    result = request_user.json()
    user_api = result['hydra:member']

    if len(user_api) > 0: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    #return 'creation compte'
    data = {
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : email,
        "password" : password1, 
        "active" : True,
        "created_at" : '',
        "updated_at" : '',
        "last_connection": ''
    }

    headers = {
        'accept': 'application/ld+json',
        'Content-Type': 'application/ld+json',
    }
    # create new user with the form data. Hash the password so plaintext version isn't saved.
    res = requests.post('http://localhost:9000/api/users', json=data, headers=headers)
    if res.ok:
        flash('Félicitation votre compte vient d\'été crée!')
        return redirect(url_for('auth.login'))
    else:
        return "error : {}".format(res)
        
@auth.route('/forgot_password')
def forget_password():
    return render_template('forgot_password.html')

@auth.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    logout_user()
    return redirect(url_for('main.index'))