from app import db
from datetime import datetime


class Product(db.Document): # Define the Product model
    name = db.StringField(required=True)  # This is the field called "name" in the database
    description = db.StringField()  # This is the field called "description" in the database
    date_created = db.DateTimeField(default=datetime.utcnow) # This is the field called "date_created" in the database
    base_price = db.FloatField() # This is the field called "base_price" in the database
    retail_price = db.FloatField() # This is the field called "retail_price" in the database
    wholesale_price = db.FloatField() # This is the field called "wholesale_price" in the database
