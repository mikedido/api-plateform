# main.py

from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    return redirect(url_for('auth.login'))

@main.route('/planes')
def plane():
    if 'loggedin' in session:
        return render_template('plane.html', name=session['username'])
    return redirect(url_for('auth.login'))

@main.route('/flights')
def flight():
    if 'loggedin' in session:
        return render_template('flight.html', name=session['username'])
    return redirect(url_for('auth.login'))
