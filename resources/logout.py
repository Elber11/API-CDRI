from core.resource_core import BaseResource

from flask_jwt_extended import get_raw_jwt
from flask_jwt_extended import jwt_required

class LogOut(BaseResource):
	def __init__(self, blacklist):
		self.blacklist = blacklist

	def check_if_token_in_blacklist(self, decrypted_token):
		jti = decrypted_token['jti']
		return jti in self.blacklist
    
	@jwt_required
	def logout(self):
		jti = get_raw_jwt()['jti']
		self.blacklist.add(jti)
		return self.make_response({"OK": "Session cerrada con éxito"}, 200)
    
	logout.methods = ["DELETE"]
