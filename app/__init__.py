from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from dotenv import load_dotenv
from config import Config


load_dotenv() # Load environment variables from .env file
db = MongoEngine() # Initialize MongoDB connection
jwt = JWTManager() # Initialize JWT manager

def create_app(): # Factory function to create the Flask application
    app = Flask(__name__) # Create a Flask application instance
    app.config.from_object(Config) # Load configuration from Config class
    CORS(
        app,
        resources={
            r"/auth/*": {"origins": "*"},
            r"/permissions/*": {"origins": "*"}
        },
        supports_credentials=True,
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"]
    )

    db.init_app(app) # Initialize MongoDB with the app
    jwt.init_app(app) # Initialize JWT with the app

    from app.routes.auth import auth_bp # Import authentication routes
    from app.routes.permission import permissions_bp # Import permission routes
    from app.routes.role import roles_bp # Import role routes

    app.register_blueprint(auth_bp, url_prefix="/auth") # Register authentication blueprint with URL prefix
    app.register_blueprint(permissions_bp, url_prefix="/permissions") # Register permissions blueprint with URL prefix
    app.register_blueprint(roles_bp, url_prefix="/roles") # Register role blueprint with URL prefix

    return app # Return the Flask application instance to be used in main.py
