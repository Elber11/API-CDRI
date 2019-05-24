from functools import wraps

from flask import request
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import verify_jwt_in_request_optional
from flask_jwt_extended import get_jwt_identity

from constants.permissions import ADMIN

def get_permissions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request_optional()
        identity = get_jwt_identity()

        try:
            if identity['group'] != ADMIN:
                _args = list(args)

                if len(_args) >= 3:
                    if int(_args[2]) != identity['id']:
                        return {'Not Found' : 'No se encontraron resultados'}, 404
                    _args.pop(2)
                
                _args.insert(2, identity['id'])
                args = tuple(_args)

            return fn(*args, **kwargs)

        except:
            if not 'login' in args[1]:
                return {'Unauthorized' : 'Debes autentificarte en la api primero'}, 401

            return fn(*args, **kwargs)

    return wrapper

def post_permissions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request_optional()
        identity = get_jwt_identity()

        try:
            if identity['group'] != ADMIN:
                return {'Forbidden' : 'No tienes permiso para crear recursos nuevos'}, 403
            else:
                return fn(*args, **kwargs)

        except:
            if request.path != '/users/':
                return {'Unauthorized' : 'Debes autentificarte en la api primero'}, 401

            new_args = dict(request.args.copy())
            new_args['user_status_id'] = 1
            new_args['user_level_id'] = 2
            _args = list(args)

            if len(args) > 1:
                _args.pop(1)

            _args.insert(1, new_args)
            args = tuple(_args)

            return fn(*args, **kwargs)

    return wrapper

def put_permissions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request_optional()
        identity = get_jwt_identity()

        try:
            if identity['group'] != ADMIN:
                new_args = dict(request.args.copy())

                if new_args.get('id'):
                    if int(new_args['id']) != identity['id']:
                        return {'Forbidden' : 'No tienes permiso de modificar a otros usuarios'}, 403
                        
                _args = list(args)

                if len(_args) > 1:
                    if int(args[1]['id']) != identity['id']:
                        return {'Forbidden' : 'No tienes permiso de modificar a otros usuarios'}, 403
                    _args.pop(1)

                new_args['id'] = identity['id']
                _args.insert(1, new_args)
                args = tuple(_args)

            return fn(*args, **kwargs)

        except:
            return {'Unauthorized' : 'Debes autentificarte en la api primero'}, 401

    return wrapper

def delete_permissions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()

        if identity['group'] != ADMIN:
            return {'Forbidden' : 'No tienes permiso de eliminar a otros usuarios'}, 403

        return fn(*args, **kwargs)

    return wrapper