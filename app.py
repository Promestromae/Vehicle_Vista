from flask import Flask, render_template
from .config import SQLALCHEMY_DATABASE_URI
from .models import db

def create_app():
        app = Flask(_name_)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    return app

app = create_app()

dummy_cars = [
            {"make": "Toyota", "model": "Corolla", "year": 2022, "price": 25000, "reviews": ["Reliable", "Fuel-efficient"]},
                {"make": "Honda", "model": "Civic", "year": 2022, "price": 27000, "reviews": ["Comfortable", "Great resale value"]},
                    {"make": "Ford", "model": "F-150", "year": 2022, "price": 40000, "reviews": ["Powerful", "Spacious"]},
                        {"make": "BMW", "model": "X5", "year": 2021, "price": 60000, "reviews": ["Luxurious", "High-performance"]},
                            {"make": "Mercedes-Benz", "model": "E-Class", "year": 2020, "price": 55000, "reviews": ["Elegant design", "Advanced technology"]},
                                {"make": "Lamborghini", "model": "Aventador", "year": 2021, "price": 400000, "reviews": ["Exotic", "Extreme performance"]}
                                ]

@app.route('/')
def home():
        return render_template('index.html', cars=dummy_cars)

@app.route('/car/<int:car_id>')
def car_details(car_id):
        car = dummy_cars[car_id - 1]
    return render_template('car_details.html', car=car)

if _name_ == '_main_':
        app.run(debug=True)
