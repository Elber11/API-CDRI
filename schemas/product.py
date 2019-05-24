from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.product import Product as ModelProduct
from models.product import ProductStatus as ModelProductStatus
from models.product import ProductCategory as ModelProductCategory
from models.product import ProductCommercialBrand as ModelProductCB

class Product(BaseSchemas):
	__model__ = ModelProduct

	id = fields.Integer()
	name = fields.String(requiered=True)
	product_status_id = fields.Integer(requiered=True, load_only=True)
	product_status = fields.Nested('ProductStatus', data_key='product_status_id', dump_only=True)
	product_category_id = fields.Integer(requiered=True, load_only=True)
	product_category = fields.Nested('ProductCategory', data_key='product_category_id', dump_only=True)
	product_commercial_brand_id = fields.Integer(requiered=True, load_only=True)
	product_commercial_brand = fields.Nested('ProductCommercialBrand', data_key='product_commercial_brand_id', dump_only=True)
	model = fields.String(requiered=True)
	existence =fields.Integer()
	price = fields.Float(requiered=True)

	__filtering__ = ['id', 'name', 'product_status_id', 'product_commercial_brand_id', 'product_category_id', 'model', 'existence', 'price']

class ProductStatus(BaseSchemas):
	__model__ = ModelProductStatus

	id = fields.Integer()
	code = fields.String(requiered=True)
	description = fields.String(requiered=True)

	__filtering__ = ['id', 'code', 'description']

class ProductCategory(BaseSchemas):
	__model__ = ModelProductCategory

	id = fields.Integer()
	name = fields.String(requiered=True)
	creation_date = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)

	__filtering__ = ['id', 'name']


class ProductCommercialBrand(BaseSchemas):
	__model__ = ModelProductCB

	id = fields.Integer()
	name = fields.String(requiered=True)
	creation_date = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)

	__filtering__ = ['id', 'name']