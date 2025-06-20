from app import db


class User(db.Document): # Define a User model
    meta = {'collection': 'users'} # This is the collection name in the database
    mail = db.StringField(required=True, unique=True) # This is the field called "mail" in the database
    password = db.StringField(required=True) # This is the field called "password" in the database
    username = db.StringField(required=True, unique=True) # This is the field called "username" in the database
    secret_question = db.StringField(required=True) # This is the field called "secret_question" in the database
    secret_answer = db.StringField(required=True) # This is the field called "secret_answer" in the database
    birth_date = db.DateTimeField(required=True) # This is the field called "birth_date" in the database
    role = db.StringField(required=True) # This is the field called "role" in the database
    status = db.BooleanField(default=True) # This is the field called "status" in the database
