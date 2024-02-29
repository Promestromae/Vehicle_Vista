from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Car
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequestKeyError
from . import db

auth = Blueprint('auth', __name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}  # Allowed image extensions

@auth.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            model = request.form.get('model')
            description = request.form.get('description')
            car_image = request.files['car_image']
            engine = request.form.get('engine')

            # Check for required fields and data types
            if not name or not isinstance(name, str):
                raise BadRequestKeyError('Missing or invalid name')
            if not model or not isinstance(model, str):
                raise BadRequestKeyError('Missing or invalid model')
            if not description or not isinstance(description, str):
                raise BadRequestKeyError('Missing or invalid description')
            if not car_image:
                raise BadRequestKeyError('Missing car image')
            if not engine or not isinstance(engine, str):
                raise BadRequestKeyError('Missing or invalid engine type')

            # Check allowed file extensions
            if car_image.filename and not allowed_file(car_image.filename):
                raise ValueError('Invalid image format')

            filename = secure_filename(car_image.filename)
            image_path = os.path.join('website/static/images', filename)
            car_image.save(image_path)

            new_car = Car(name=name, model=model, description=description, image_url=image_path, engine=engine)
            db.session.add(new_car)
            db.session.commit()

            flash('Car added successfully.', 'success')
            return redirect(url_for('auth.add_car'))

        except (BadRequestKeyError, ValueError) as e:
            flash(str(e), 'danger')
            return render_template('car_form.html', user=current_user)

    return render_template('car_form.html', user=current_user)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
