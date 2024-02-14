from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Car
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
                    name = request.form.get('name')
        model = request.form.get('model')
        description = request.form.get('description')
        car_image = request.files['car_image']
        engine = request.form.get('engine')

        # Check if any of the fields are empty
        if not name:
                        flash('Name is required.', 'warning')
        if not model:
                        flash('Model is required.', 'warning')
        if not description:
                        flash('Description is required.', 'warning')
        if not car_image:
                        flash('Car image is required.', 'warning')
        if not engine:
                        flash('Engine type is required.', 'warning')

        # Only proceed if all fields are provided
        if name and model and description and car_image and engine:
                        filename = secure_filename(car_image.filename)
            image_path = os.path.join('website/static/images', filename)
            car_image.save(image_path)

            new_car = Car(name=name, model=model, description=description, image_url=image_path, engine=engine)
            db.session.add(new_car)
            db.session.commit()

            flash('Car added successfully.', 'success')
            return redirect(url_for('auth.add_car'))

    return render_template('car_form.html', user=current_user)
