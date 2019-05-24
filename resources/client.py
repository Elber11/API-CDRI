from flask import request

from core.resource_core import BaseResource
from schemas.client import Client as SchemaClient
from schemas.client import ClientType as SchemaClientType
from schemas.client import ClientStatus as SchemaClientStatus

class Client(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH, PARTIAL_DELETE, DELETE'}

	def client_r(self):
		if request.method == 'GET':
			response, code = SchemaClient.get()
			
		elif request.method == 'POST':
			client = SchemaClient()
			args = dict(request.args.copy())
			args['client_status_id'] = 1
			response, code = client.post(args)

		elif request.method == 'PUT':
			client = SchemaClient()
			response, code = client.put()

		elif request.method == 'PATCH':
			client = SchemaClient()
			response, code = client.patch()			

		elif request.method == 'PARTIAL_DELETE':
			client = SchemaClient()
			response, code = client.partial_delete('client_status_id')

		elif request.method == 'DELETE':
			client = SchemaClient()
			response, code = client.delete()

		return self.make_response(response, code, self.header)

	client_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class ClientType(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def client_type_r(self):
		if request.method == 'GET':
			response, code = SchemaClientType.get()
			
		elif request.method == 'POST':
			client_type = SchemaClientType()
			response, code = client_type.post()

		elif request.method == 'PUT':
			client_type = SchemaClientType()
			response, code = client_type.put()

		elif request.method == 'PATCH':
			client_type = SchemaClientType()
			response, code = client_type.patch()

		return self.make_response(response, code, self.header)

	client_type_r.methods = ['GET', 'POST', 'PUT', 'PATCH']

class ClientStatus(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def client_status_r(self):
		if request.method == 'GET':
			response, code = SchemaClientStatus.get()
			
		elif request.method == 'POST':
			client_status = SchemaClientStatus()
			response, code = client_status.post()

		elif request.method == 'PUT':
			client_status = SchemaClientStatus()
			response, code = client_status.put()

		elif request.method == 'PATCH':
			client_status = SchemaClientStatus()
			response, code = client_status.patch()

		return self.make_response(response, code, self.header)
		
	client_status_r.methods = ['GET', 'POST', 'PUT', 'PATCH']