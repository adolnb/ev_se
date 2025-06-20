from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.permission import Permission

permissions_bp = Blueprint('permissions', __name__)

@permissions_bp.route('/list', methods=['GET'])
@jwt_required()
def list_permissions():
    perms = Permission.objects()
    return jsonify([{"id": str(p.id), "name": p.name} for p in perms])


@permissions_bp.route('/create', methods=['POST'])
@jwt_required()
def create_permission():
    data = request.get_json()
    perm = Permission(name=data['name']).save()
    return jsonify(id=str(perm.id), message="Permission created"), 201


@permissions_bp.route('/update/<perm_id>', methods=['PUT'])
@jwt_required()
def update_permission(perm_id):
    data = request.get_json()
    Permission.objects(id=perm_id).update_one(set__name=data['name'])
    return jsonify(message="Permission updated")


@permissions_bp.route('/delete/<perm_id>', methods=['DELETE'])
@jwt_required()
def delete_permission(perm_id):
    Permission.objects(id=perm_id).delete()
    return jsonify(message="Permission deleted")
