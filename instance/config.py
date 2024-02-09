import os

# Define the base directory of the project
basedir = os.path.abspath(os.path.dirname(_file_))

class Config:
        # Secret key for CSRF protection and session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    # SQLite database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data', 'vehicle_vista.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = os.environ.get('DEBUG') or False
