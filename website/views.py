from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Car, Recommendations, Search
from . import db

views = Blueprint('views', _name_)

@views.route('/')
def home():
        cars = Car.query.all()
    return render_template("home.html", user=current_user, cars=cars)

@views.route('/car/<int:car_id>')
def view_car(car_id):
        car = Car.query.get_or_404(car_id)
    return render_template('car_detail.html', car=car)

@views.route('/dashboard')
@login_required
def dashboard():
        return render_template('dashboard.html')

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
        if request.method == 'POST':
                    criteria = request.form['criteria']
        search_results = Search.query.filter_by(criteria=criteria).all()
        return render_template('search_results.html', search_results=search_results)
    return render_template('search.html')

@views.route('/recommendations')
@login_required
def recommendations():
        user_id = current_user.id
    recommended_cars = Recommendations.query.filter_by(user_id=user_id).all()
    return render_template('recommendations.html', recommended_cars=recommended_cars)
