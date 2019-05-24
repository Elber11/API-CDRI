from flask import request

from core.resource_core import BaseResource
from schemas.sale import Sale as SchemaSale
from schemas.sale import SaleStatus as SchemaSaleStatus

class Sale(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH, PARTIAL_DELETE, DELETE'}

	def sale_r(self):
		if request.method == 'GET':
			response, code = SchemaSale.get()
			
		elif request.method == 'POST':
			sale = SchemaSale()
			args = dict(request.args.copy())
			args['sale_status_id'] = 2
			response, code = sale.post(args)

		elif request.method == 'PUT':
			sale = SchemaSale()
			response, code = sale.put()

		elif request.method == 'PATCH':
			sale = SchemaSale()
			response, code = sale.patch()

		elif request.method == 'PARTIAL_DELETE':
			sale = SchemaSale()
			response, code = sale.partial_delete('sale_status_id')

		elif request.method == 'DELETE':
			sale = SchemaSale()
			response, code = sale.delete()

		return self.make_response(response, code, self.header)

	sale_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class SaleStatus(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def sale_status_r(self):
		if request.method == 'GET':
			response, code = SchemaSaleStatus.get()
			
		elif request.method == 'POST':
			sale_status = SchemaSaleStatus()
			response, code = sale_status.post()

		elif request.method == 'PUT':
			sale_status = SchemaSaleStatus()
			response, code = sale_status.put()

		elif request.method == 'PATCH':
			sale_status = SchemaSaleStatus()
			response, code = sale_status.patch()

		return self.make_response(response, code, self.header)
		
	sale_status_r.methods = ['GET', 'POST', 'PUT', 'PATCH']