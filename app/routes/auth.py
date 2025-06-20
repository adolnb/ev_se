from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from datetime import datetime


auth_bp = Blueprint('auth', __name__) # Authentication blueprint

@auth_bp.route('/secret-questions', methods=['GET']) # Route to get the secret questions
def get_secret_questions(): # Funtion to handle the request for secret questions
    questions = [ # List of secret questions
        "What was the name of your first pet?",
        "What was your childhood nickname?",
        "Your favorite video game buddy?",
        "What is your PR dear monster?",
        "What is your dream car?",
        "Where were you born?",
        "What is your favorite position ever (about any topic)?"
    ]
    return jsonify(questions), 200 # Return the list of questions in JSON format with status code 200 (OK)


@auth_bp.route('/register', methods=['POST']) # Route for user registration
def register(): # Function to handle user registration
    data = request.get_json() # Get JSON data from request
    if User.objects(mail=data['mail']).first(): # Check if user data is already exists
        return jsonify(message="The mail is already in use."), 400 # Return a error message with status code 400 (Bad Request)
    if User.objects(username=data['username']).first(): # Check if user data is already exists
        return jsonify(message="The username is already in use. Please choose another one."), 400 # Return a error message with status code 400 (Bad Request)
    hashed_pw = generate_password_hash(data['password']) # Hash the password using werkzeug seccurity (this is a package that provides password hashing utilities)
    try:
        birth_date = datetime.strptime(data['birth_date'], "%Y-%m-%d")  # Convert the birth_date string to a datetime object
    except ValueError:
        return jsonify(message="Invalid birth date format."), 400 # Return an error message with status code 400 (Bad Request)
    user = User(
        username=data['username'],
        password=hashed_pw,
        mail=data['mail'],
        secret_question=data['secret_question'],
        secret_answer=data['secret_answer'],
        birth_date=birth_date,
        role="6847e4ed3337a432a03d2710", 
    ) # Create a newUser instance with username and hashed password
    user.save() # Save the user to the database
    return jsonify(message="If you wanna be an slave, congratulations!! have a contract with us for all your life buddy."), 201 # Return a success message with status code 201 (Created)


@auth_bp.route('/login', methods=['POST']) # Route for user login
def login(): # Function to handle user login
    data = request.get_json() # Get JSON data from request
    user = User.objects(mail=data['mail']).first() # Find the user by email
    if user and check_password_hash(user.password, data['password']): # Check if user exists and password matches
        token = create_access_token(identity=str(user.id)) # Create a JWT token with user ID as identity
        return jsonify({
            "access_token": token,
        }) # Return the token in JSON format
    return jsonify(message="Invalid credentials. WTF are you wanna do dude?"), 401 # Return a error message with status code 401 (Unauthorized)
        