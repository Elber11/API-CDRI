from flask import request

from core.resource_core import BaseResource
from schemas.inventory_flow import InventoryFlow as SchemaInventoryFlow
from schemas.inventory_flow import InventoryFlowType as SchemaInventoryFlowType
from schemas.product import Product
from core.sqlalchemy import db

class InventoryFlow(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH, PARTIAL_DELETE, DELETE'}

	def inventory_flow_r(self):
		if request.method == 'GET':
			response, code = SchemaInventoryFlow.get()
			
		elif request.method == 'POST':
			inventory_flow = SchemaInventoryFlow()
			product = Product()
			response, code = inventory_flow.post()

			if code == 201:
				_type = int(request.args['inventory_flow_type_id'])

				if _type == 1:
					product = Product.__model__.query.filter_by(id=request.args['product_id']).first()
					product.product_status_id = 2
					product.existence += int(request.args['quantity'])
					product.price = float(request.args['unity_price'])
					db.session.add(product)
					db.session.commit()

		elif request.method == 'PUT':
			inventory_flow = SchemaInventoryFlow()
			response, code = inventory_flow.put()

		elif request.method == 'PATCH':
			inventory_flow = SchemaInventoryFlow()
			response, code = inventory_flow.patch()

		elif request.method == 'PARTIAL_DELETE':
			inventory_flow = SchemaInventoryFlow()
			response, code = inventory_flow.partial_delete('inventory_flow_status_id')

		elif request.method == 'DELETE':
			inventory_flow = SchemaInventoryFlow()
			response, code = inventory_flow.delete()

		return self.make_response(response, code, self.header)

	inventory_flow_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class InventoryFlowType(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def inventory_flow_type_r(self):
		if request.method == 'GET':
			response, code = SchemaInventoryFlowType.get()
			
		elif request.method == 'POST':
			inventory_flow_type = SchemaInventoryFlowType()
			response, code = inventory_flow_type.post()

		elif request.method == 'PUT':
			inventory_flow_type = SchemaInventoryFlowType()
			response, code = inventory_flow_type.put()

		elif request.method == 'PATCH':
			inventory_flow_type = SchemaInventoryFlowType()
			response, code = inventory_flow_type.patch()

		return self.make_response(response, code, self.header)

	inventory_flow_type_r.methods = ['GET', 'POST', 'PUT', 'PATCH']