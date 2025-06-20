from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.product import Product


products_bp = Blueprint('products', __name__) # Blueprint for product-related routes

@products_bp.route('/', methods=['GET']) # Route for listing all products
@jwt_required()

def list_products(): # Function to handle listing products
    products = Product.objects() # Fetch all products from the database
    return jsonify(products), 200 # Return products as JSON with status code 200 (OK)

@products_bp.route('/', methods=['POST']) # Route for creating a new product
@jwt_required() # JWT required for access
def create_product(): # Function to handle product creation
    data = request.get_json() # Get JSON data from the request
    product = Product(**data) # Create a neww product instance with the provided data
    product.save() # Save the productt to the database
    return jsonify(message="Producto creado"), 201 # Return success message with status code 201 (Created)

@products_bp.route('/<product_id>', methods=['PUT']) # Route for updating a product
@jwt_required() # JWT required for access
def update_product(product_id): # Function to handle product update
    data = request.get_json() # Get JSON data from the request
    product = Product.objects(id=product_id).first() # Fetch the product by ID
    if not product: # If product is not found
        return jsonify(message="Producto no encontrado"), 404 # Return error message with status code 404 (Not Found)
    product.update(**data) # Update thhe product with the provided data
    return jsonify(message="Producto actualizado"), 200 # Return success message with status code 200 (OK)

@products_bp.route('/<product_id>', methods=['DELETE']) # Route for deleting a product
@jwt_required() # JWT required for access
def delete_product(product_id): # Function to handle product deletion
    product = Product.objects(id=product_id).first() # Fetch the product by ID
    if not product: # If product is not found
        return jsonify(message="Producto no encontrado"), 404 # Return error messagee with status code 404 (Not Found)
    product.delete() # Delete the product from the database
    return jsonify(message="Producto eliminado"), 200 # Return success message with status code 200 (OK)
