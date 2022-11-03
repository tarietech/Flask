from enum import unique
from . import db 
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))  
    username = db.Column(db.String(150), unique=True)
    surname = db.Column(db.String(150))



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True )
    name = db.Column(db.String(length=30), nullable=False, unique=True )
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
   

class Stock(db.Model):
    id = db.Column(db.Integer(), primary_key=True )
    name = db.Column(db.String(length=30), nullable=False, unique=True )
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    

