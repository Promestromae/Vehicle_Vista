from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'  # Replace with your database connection string
db = SQLAlchemy(app)

class Car(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  model = db.Column(db.String(80), nullable=False)
  description = db.Column(db.Text, nullable=False)
  car_image = db.Column(db.String(120))
  engine = db.Column(db.String(40), nullable=False)

  def __repr__(self):
    return f"{self.name} {self.model}"

class CarForm(FlaskForm):
  name = StringField('Name', validators=[validators.DataRequired(), validators.Length(min=2, max=80, message="Name must be between 2 and 80 characters")])
  model = StringField('Model', validators=[validators.DataRequired(), validators.Length(min=2, max=80, message="Model must be between 2 and 80 characters")])
  description = TextAreaField('Description', validators=[validators.DataRequired(), validators.Length(min=10, message="Description must be at least 10 characters")])
  car_image = FileField('Car Image', validators=[validators.Optional()])
  engine = StringField('Engine Type', validators=[validators.DataRequired(), validators.Length(min=2, max=40, message="Engine type must be between 2 and 40 characters")])
  submit = SubmitField('Submit')

@app.route('/')
def home():
  cars = Car.query.all()
  return render_template('car_list.html', cars=cars)

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
  form = CarForm()
  if form.validate_on_submit():
    # Extract data from the form
    name = form.name.data
    model = form.model.data
    description = form.description.data
    car_image = form.car_image.data  # Assuming you handle file uploads appropriately
    engine = form.engine.data

    # Create a new car object
    new_car = Car(name=name, model=model, description=description, car_image=car_image, engine=engine)

    # Add to database
    db.session.add(new_car)
    db.session.commit()

    # Success message
    success_message = "Car added successfully!"
    return redirect(url_for('home'))  # Redirect to car list page
  else:
    # Handle invalid form
    error_messages = form.errors.items()
  return render_template('car_form.html', form=form, success_message=success_message, error_messages=error_messages)

@app.route('/update_car/<int:car_id>', methods=['GET', 'POST'])
def update_car(car_id):
  try:
    car = Car.query.get(car_id)  # Retrieve car object by ID
  except:
    # Handle car not found error (e.g., display an error message)
    return render_template('error.html', error_message="Car not found!")

  form = CarForm(obj=car)  # Pre-populate form with existing data

  if form.validate_on_submit():
    # Update existing car object with form data
    car.name = form.name.data
    car.model = form.model.data
    car.description = form.description.data
    car_image = form.car_image.data  # Assuming you handle file uploads appropriately
    if car_image:
      car.car_image = car_image
    car.engine = form.engine.data
