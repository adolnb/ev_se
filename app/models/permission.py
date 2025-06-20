from app import db


class Permission(db.Document): # Define the Permission model
    meta = {'collection': 'permissions'}
    name = db.StringField(required=True, unique=True) # This is the field called "name" in the database