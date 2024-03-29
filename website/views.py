from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Car, Recommendations, Search
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    cars = Car.query.all()
    return render_template("home.html", user=current_user, cars=cars)


@views.route('/car/<int:car_id>')
def view_car(car_id):
    car = Car.query.get(car_id)  # Use Car.query.get directly
    if not car:
        return abort(404)  # Handle case where car is not found
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
    try:
        recommendations = get_recommendations(user_id)  # Call the function directly
        if 'error_message' in recommendations:
            flash(recommendations['error_message'], 'error')
            return render_template('recommendations.html', recommended_cars=[])

        recommended_cars = recommendations['recommended_cars']
        total_cars = recommendations['total_cars']
        average_price = recommendations['average_price']

        return render_template('recommendations.html', recommended_cars=recommended_cars,
                               total_cars=total_cars, average_price=average_price)

    except Exception as e:
        # Handle unexpected errors (log for debugging)
        current_app.logger.error(f"Error retrieving recommendations: {str(e)}")
        flash('An error occurred while fetching recommendations. Please try again later.', 'error')
        return render_template('recommendations.html', recommended_cars=[])
