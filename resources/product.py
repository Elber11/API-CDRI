from flask import request

from core.resource_core import BaseResource
from schemas.product import Product as SchemaProduct
from schemas.product import ProductCategory as SchemaProductCategory
from schemas.product import ProductStatus as SchemaProductStatus
from schemas.product import ProductCommercialBrand as SchemaProductCB

class Product(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH, PARTIAL_DELETE, DELETE'}

	def product_r(self):
		if request.method == 'GET':
			response, code = SchemaProduct.get()
			
		elif request.method == 'POST':
			product = SchemaProduct()
			args = dict(request.args.copy())
			args['product_status_id'] = 3
			args['existence'] = 0
			args['price'] = 0
			response, code = product.post(args)

		elif request.method == 'PUT':
			product = SchemaProduct()
			response, code = product.put()

		elif request.method == 'PATCH':
			product = SchemaProduct()
			response, code = product.patch()

		elif request.method == 'PARTIAL_DELETE':
			product = SchemaProduct()
			response, code = product.partial_delete('product_status_id')

		elif request.method == 'DELETE':
			product = SchemaProduct()
			response, code = product.delete()

		return self.make_response(response, code, self.header)

	product_r.methods = ['GET', 'POST', 'PUT', 'PATCH', 'PARTIAL_DELETE', 'DELETE']

class ProductCategory(BaseResource):
	header = {'Allow' : 'GET, POST, PATCH, PUT'}

	def product_category_r(self):
		if request.method == 'GET':
			response, code = SchemaProductCategory.get()
			
		elif request.method == 'POST':
			product_category = SchemaProductCategory()
			response, code = product_category.post()

		elif request.method == 'PUT':
			product_category = SchemaProductCategory()
			response, code = product_category.put()

		elif request.method == 'PATCH':
			product_category = SchemaProductCategory()
			response, code = product_category.patch()

		return self.make_response(response, code, self.header)

	product_category_r.methods = ['GET', 'POST', 'PUT', 'PATCH']

class ProductStatus(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def product_status_r(self):
		if request.method == 'GET':
			response, code = SchemaProductStatus.get()
			
		elif request.method == 'POST':
			product_status = SchemaProductStatus()
			response, code = product_status.post()

		elif request.method == 'PUT':
			product_status = SchemaProductStatus()
			response, code = product_status.put()

		elif request.method == 'PATCH':
			product_status = SchemaProductStatus()
			response, code = product_status.patch()

		return self.make_response(response, code, self.header)
		
	product_status_r.methods = ['GET', 'POST', 'PUT', 'PATCH']


class ProductCommercialBrand(BaseResource):
	header = {'Allow' : 'GET, POST, PUT, PATCH'}

	def product_commercial_brand_r(self):
		if request.method == 'GET':
			response, code = SchemaProductCB.get()
			
		elif request.method == 'POST':
			product_commercial_brand = SchemaProductCB()
			response, code = product_commercial_brand.post()

		elif request.method == 'PUT':
			product_commercial_brand = SchemaProductCB()
			response, code = product_commercial_brand.put()

		elif request.method == 'PATCH':
			product_commercial_brand = SchemaProductCB()
			response, code = product_commercial_brand.patch()

		return self.make_response(response, code, self.header)

	product_commercial_brand_r.methods = ['GET', 'POST', 'PUT', 'PATCH']