from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.inventory_flow import InventoryFlow as ModelInvetoryFlow
from models.inventory_flow import InventoryFlowType as ModelInvetoryFlowType
from schemas.provider import Provider
from schemas.product import Product


class InventoryFlow(BaseSchemas):
	__model__ = ModelInvetoryFlow

	id = fields.Integer()
	inventory_flow_type_id = fields.Integer(requiered=True, load_only=True)
	inventory_flow = fields.Nested('InventoryFlow', data_key='inventory_flow_id', dump_only=True)
	provider_id = fields.Integer(allow_none=True, load_only=True)
	provider = fields.Nested(Provider, data_key='provider_id', dump_only=True)
	product_id = fields.Integer(requiered=True, load_only=True)
	product = fields.Nested(Product, data_key='product_id', dump_only=True)
	quantity = fields.Integer(requiered=True)
	unity_price = fields.Float(requiered=True)
	total_price = fields.Float(requiered=True)
	datetime = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)

	__filtering__ = ['id', 'inventory_flow_type_id', 'provider_id', 'product_id', 'quantity', 'unity_price', 'total_price']


class InventoryFlowType(BaseSchemas):
	__model__ = ModelInvetoryFlowType

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']