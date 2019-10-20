# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/plane')
@login_required
def plane():
    return render_template('plane.html', name=current_user.name)

@main.route('/flight')
@login_required
def flight():
    return render_template('flight.html', name=current_user.name)