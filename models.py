from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_migrate import Migrate
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/flaskapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#1. Model for patient Details
class Patient_details(db.Model):
    _tablename_ ='patient_details'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    name = db.Column(db.Text, unique=False, nullable=False)
    age = db.Column(db.Text,unique=False,nullable = False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique = False, nullable=False)
    contact = db.Column(db.Text, unique=False, nullable=False)
    gender = db.Column(db.Text, unique=False, nullable=False)
    address=db.Column(db.String(100), unique=False, nullable=False)