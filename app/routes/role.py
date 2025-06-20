from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.role import Role


roles_bp = Blueprint('roles', __name__) # Blueprint for roles and permission

@roles_bp.route('/create', methods=['POST']) # Create a new role
@jwt_required() # JWT required for access
def create_role(): # Function to handle role creation
    data = request.get_json() # Get JSON data from the request
    role = Role(name=data['name']).save() # Create a new role with the provided name and permissions, then save it to the database
    return jsonify(message="Rol creado", id=str(role.id)), 201 # Return success message with role ID with status code 201 (Created)


@roles_bp.route('/list', methods=['GET'])
@jwt_required()
def list_roles():
    roles = Role.objects().only('name', 'permissions')
    return jsonify([
        {
            "id": str(role.id),
            "name": role.name,
            "permissions": [str(pid) for pid in role.permissions]
        } for role in roles
    ])


@roles_bp.route('/update/<role_id>', methods=['PUT'])
@jwt_required()
def update_role(role_id):
    data = request.get_json()
    Role.objects(id=role_id).update_one(
        set__name=data['name'],
        set__permissions=data.get('permissions', [])
    )
    return jsonify(message="Role updated")


@roles_bp.route('/delete/<role_id>', methods=['DELETE'])
@jwt_required()
def delete_role(role_id):
    Role.objects(id=role_id).delete()
    return jsonify(message="Role deleted")
