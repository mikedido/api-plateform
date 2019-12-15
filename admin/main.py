# main.py

from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user
import requests, math

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

@main.route('/flights', defaults={"page":'1'})
@main.route('/flights/<page>')
def flight(page):
    if 'loggedin' in session:
        #parse the result of the API call
        request_flights = requests.get('http://localhost:9000/api/flights?page='+page)
        result = request_flights.json()
        flight_api = result['hydra:member']

        page_number_count=math.ceil(result['hydra:totalItems']/30)
        return render_template('flight.html', name=session['username'], 
            flights=flight_api, 
            page_count=page_number_count+1, 
            current_page=page)
    return redirect(url_for('auth.login'))

@main.route('/flights/add')
def add_flight():
    return render_template('add_flight.html')