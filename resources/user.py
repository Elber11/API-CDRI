from flask import request

from core.resource_core import BaseResource
from schemas.user import User as SchemaUser
from schemas.user import UserLevel as SchemaUserLevel
from schemas.user import UserStatus as SchemaUserStatus

class User(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH, PARTIAL_DELETE, DELETE'}

	def user_r(self):
		if request.method == 'GET':
			response, code = SchemaUser.get()
			
		elif request.method == 'POST':
			user = SchemaUser()
			args = dict(request.args.copy())
			args['user_status_id'] = 1
			args['user_level_id'] = 2
			response, code = user.post(args)

		elif request.method == 'PUT':
			user = SchemaUser()
			response, code = user.put()

		elif request.method == 'PATCH':
			user = SchemaUser()
			response, code = user.patch()

		elif request.method == 'PARTIAL_DELETE':
			user = SchemaUser()
			response, code = user.partial_delete('user_status_id')

		elif request.method == 'DELETE':
			user = SchemaUser()
			response, code = user.delete()

		return self.make_response(response, code, self.header)

	user_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class UsersLevel(BaseResource):
	def user_level_r(self):
		header = {'Allow' : 'GET, POST, PUT, PATCH'}

		if request.method == 'GET':
			response, code = SchemaUserLevel.get()

		elif request.method == 'POST':
			user = SchemaUserLevel()
			response, code = user.post()

		elif request.method == 'PUT':
			user = SchemaUserLevel()
			response, code = user.put()

		elif request.method == 'PATCH':
			user = SchemaUserLevel()
			response, code = user.patch()

		return self.make_response(response, code, header)

	user_level_r.methods = ['GET', 'POST', 'PUT', 'PATCH']

class UsersStatus(BaseResource):
	def user_status_r(self):
		header = {'Allow' : 'GET, POST, PUT, PATCH'}

		if request.method == 'GET':
			response, code = SchemaUserStatus.get()

		elif request.method == 'POST':
			user = SchemaUserStatus()
			response, code = user.post()

		elif request.method == 'PUT':
			user = SchemaUserStatus()
			response, code = user.put()

		elif request.method == 'PATCH':
			user = SchemaUserStatus()
			response, code = user.patch()

		return self.make_response(response, code, header)

	user_status_r.methods = ['GET', 'POST', 'PUT', 'PATCH']