from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialize the database
db = SQLAlchemy()
DB_NAME = "vehicle_vista.db"

def create_app():
        app = Flask(_name_)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = 'static/images'  # Set the upload folder for images
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set max upload size to 16MB
    
    # Initialize the database
    db.init_app(app)

    migrate = Migrate(app, db)
    
    # Import views and auth blueprints
    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    # Import models
    from .models import User, Car, Review

    with app.app_context():
                # Create tables based on the defined models
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
                """Load a user given the user's ID."""
        return User.query.get(int(id))

    return app

def create_db(app):
        """Create the database."""
    if not path.exists('website/' + DB_NAME):
                db.create_all(app= app)
        print("Database created successfully")
