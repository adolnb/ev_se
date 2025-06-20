from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission

def require_permission(permission_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = User.objects(id=get_jwt_identity()).first()
            if not user:
                return jsonify(message="Unauthorized"), 401
            role = Role.objects(id=user.role).first()
            if not role:
                return jsonify(message="Role not found"), 403
            perm_names = [p.name for p in Permission.objects(id__in=role.permissions)]
            if permission_name not in perm_names:
                return jsonify(message="Permission denied"), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
