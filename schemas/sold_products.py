from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.sold_products import SoldProducts as ModelSoldProducts

from schemas.sale import Sale
from schemas.product import Product

class SoldProducts(BaseSchemas):
	__model__ = ModelSoldProducts

	sale_id = fields.Integer(requiered=True, load_only=True)
	sale = fields.Nested(Sale, data_key='sale_id', dump_only=True)
	product_id = fields.Integer(requiered=True, load_only=True)
	product = fields.Nested(Product, data_key='product_id', dump_only=True)
	quantity = fields.Integer(requiered=True)
	unity_price = fields.Integer(requiered=True)
	total_price = fields.Integer(requiered=True)
	
	__filtering__ = ['sale_id', 'product_id', 'quantity', 'unity_price', 'total_price']