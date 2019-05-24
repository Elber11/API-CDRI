from core.resource_core import BaseResource

class TokenErrorHandler(BaseResource):
	@classmethod
	def unauthorized_token(cls, msg):
		msg = 'Falta el token de acceso en la cabecera'
		response = {'Unauthorized' : msg, 'code' : 'MISSING_TOKEN'}

		return cls.make_response(cls, response, 401) 

	@classmethod
	def expired_token(cls, data):
		msg = 'El token ha expirado, vuelve a iniciar session para poder seguir usando la api'
		response = {'Unauthorized' : msg, 'code' : 'TOKEN_EXPIRE'}

		return cls.make_response(cls, response, 401) 
    
	@classmethod
	def revoken_token(cls):
		msg = 'El token ha sido revocado, vuelve a iniciar session para poder usar la api'
		response = {'Unauthorized' : msg, 'code' : 'TOKEN_REVOKED'}
   
		return cls.make_response(cls, response, 401) 
