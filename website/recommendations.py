from flask import Blueprint, redirect, url_for
from flask_login import current_user

# Assuming you have a function to retrieve recommendations in models.py
from .models import get_recommendations

# Define a blueprint for recommendations
recommendations_bp = Blueprint('recommendations', __name__, url_prefix='/recommendations')

@recommendations_bp.route('/')
@login_required
def recommendations():
    user_id = current_user.id
    recommendations, total_cars, average_price = get_recommendations(user_id)

    if not recommendations:
        flash('An error occurred while fetching recommendations. Please try again later.', 'error')
        return redirect(url_for('index'))  # Redirect to your desired fallback page

    return render_template('recommendations.html', recommended_cars=recommendations,
                           total_cars=total_cars, average_price=average_price)
