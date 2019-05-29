from flask import request

from core.resource_core import BaseResource
from schemas.sold_products import SoldProducts as SchemaSoldProducts
from schemas.product import Product
from schemas.inventory_flow import InventoryFlow
from core.sqlalchemy import db

class SoldProducts(BaseResource):
	header = {'Allow' : 'GET, POST'}

	def sold_products_r(self, id):
		if request.method == 'GET':
			args = dict(request.args.copy())
			args['sale_id'] = id
			args['fields'] = 'product_id,quantity,unity_price,total_price'
			response, code = SchemaSoldProducts.get(args)

		elif request.method == 'POST':
			sold_products = SchemaSoldProducts()
			args = dict(request.args.copy())
			args['sale_id'] = id
			response, code = sold_products.post(args)

			if code == 201:				
				product = Product.__model__.query.filter_by(id=request.args['product_id']).first()
				product.existence -= int(request.args['quantity'])
				inventory_flow = InventoryFlow.__model__(product_id=request.args['product_id'], 
														 quantity=request.args['quantity'],
														 unity_price=request.args['unity_price'],
														 total_price=request.args['total_price'],
														 inventory_flow_type_id=2
														 )

				if product.existence == 0:
					product.product_status_id = 3

				db.session.add(product)
				db.session.commit()
				db.session.add(inventory_flow)
				db.session.commit()


		return self.make_response(response, code, self.header)
		
	sold_products_r.methods = ['GET', 'POST']