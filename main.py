from app import create_app


app = create_app() # Initialize the Flask application

if __name__ == "__main__": # Run the application
    app.run(debug=True) # Set development mode