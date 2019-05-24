from flask import request

from core.resource_core import BaseResource
from schemas.provider import Provider as SchemaProvider
from schemas.provider import ProviderReputation as SchemaProviderReputation
from schemas.provider import ProviderStatus as SchemaProviderStatus

class Provider(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH PARTIAL_DELETE, DELETE'}

	def provider_r(self):
		if request.method == 'GET':
			response, code = SchemaProvider.get()
			
		elif request.method == 'POST':
			provider = SchemaProvider()
			args = dict(request.args.copy())
			args['provider_status_id'] = 1
			args['provider_reputation_id'] = 2
			response, code = provider.post(args)

		elif request.method == 'PUT':
			provider = SchemaProvider()
			response, code = provider.put()

		elif request.method == 'PATCH':
			provider = SchemaProvider()
			response, code = provider.patch()

		elif request.method == 'PARTIAL_DELETE':
			provider = SchemaProvider()
			response, code = provider.partial_delete('provider_status_id')

		elif request.method == 'DELETE':
			provider = SchemaProvider()
			response, code = provider.delete()

		return self.make_response(response, code, self.header)

	provider_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class ProviderReputation(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def provider_reputation_r(self):
		if request.method == 'GET':
			response, code = SchemaProviderReputation.get()
			
		elif request.method == 'POST':
			provider_type = SchemaProviderReputation()
			response, code = provider_type.post()

		elif request.method == 'PUT':
			provider_type = SchemaProviderReputation()
			response, code = provider_type.put()

		elif request.method == 'PATCH':
			provider_type = SchemaProviderReputation()
			response, code = provider_type.patch()

		return self.make_response(response, code, self.header)


	provider_reputation_r.methods = ['GET', 'POST', 'PUT', 'PATCH']

class ProviderStatus(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def provider_status_r(self):
		if request.method == 'GET':
			response, code = SchemaProviderStatus.get()
			
		elif request.method == 'POST':
			provider_status = SchemaProviderStatus()
			response, code = provider_status.post()

		elif request.method == 'PUT':
			provider_status = SchemaProviderStatus()
			response, code = provider_status.put()

		elif request.method == 'PATCH':
			provider_status = SchemaProviderStatus()
			response, code = provider_status.patch()

		return self.make_response(response, code, self.header)
		

	provider_status_r.methods = ['GET', 'POST', 'PUT', 'PATCH']