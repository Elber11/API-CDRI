from flask import request
from flask_jwt_extended import create_access_token

from core.resource_core import BaseResource
from schemas.user import User

class Login(BaseResource):
	def login(self):
		if not 'name' in request.args:
			return self.make_response({'Bad Request' : 'Falta el parametro name'}, 400)

		if not 'password' in request.args:
			return self.make_response({'Bad Request' : 'Falta el parametro password'}, 400)

		request_args = dict(request.args.copy())
		name = request_args['name']
		password = request_args['password']
		user = User.__model__.query.filter_by(name=name, password=password).first()

		if not user:
			return self.make_response({'Not Found' : 'El nombre de usuario o contraseña es incorrecto'}, 404)

		id = user.id
		name = user.name
		group = user.user_level_id
		status = user.user_status_id
		
		if status == -1:
			return self.make_response({'Unauthorized' : 'Este usuario fue eliminado'}, 401)

		identity = {
                    	'id' : id,
                   		'name' : name,
                    	'group' : group
                    }
        
		response = {
                        'access_token' : create_access_token(identity=identity)
                    }


		return self.make_response(response, 200)

	login.methods = ['POST']