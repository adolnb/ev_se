from app import db
from bson import ObjectId


class Role(db.Document): # Define the Role model
    meta = {'collection': 'roles'}
    name = db.StringField(required=True, unique=True) # This is the field called "name" in the database
    permissions = db.ListField(db.ObjectIdField()) # This is the field called "permissions" in the database