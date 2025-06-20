import os
from dotenv import load_dotenv


load_dotenv() # Load enviroment variables from .env file
class Config: # Base configuration class
    SECRET_KEY = os.getenv("SECRET_KEY") # Secret key but for session management
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") # Secret key for JWT tokens
    JWT_ACCESS_TOKEN_EXPIRES = 300 # 5 minutes

    MONGODB_SETTINGS = {
        'db': os.getenv("MONGODB_DB"), # Database name
        'host': os.getenv("MONGODB_URI") # Connection URI
    }
