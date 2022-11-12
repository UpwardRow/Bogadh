from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Application definition
app = Flask(__name__)

# Creating a bytes object which contains random bytes for use of Flask secret key
SECRET_KEY = os.urandom(1000)

# Configuration variables
# Connection string to connect to database with an environmental variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

# Database class
db = SQLAlchemy(app)

# This import is at the bottom of the application because if it is at the top level, it causes a circular import error
from application import routes
