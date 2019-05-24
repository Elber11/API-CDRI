from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.sale import Sale as ModelSale
from models.sale import SaleStatus as ModelSaleStatus

from schemas.client import Client
from schemas.user import User

class Sale(BaseSchemas):
	__model__ = ModelSale

	id = fields.Integer()
	user_id = fields.Integer(required=True, load_only=True)
	user = fields.Nested(User, data_key='user_id', dump_only=True)
	client_id = fields.Integer(required=True, load_only=True)
	client = fields.Nested(Client, data_key='client_id', dump_only=True)
	sale_status_id = fields.Integer(required=True, load_only=True)
	sale_status = fields.Nested('SaleStatus', data_key='sale_status_id', dump_only=True)
	creation_date = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)
	
	__filtering__ = ['id', 'user_id', 'client_id', 'sale_status_id']

class SaleStatus(BaseSchemas):
	__model__ = ModelSaleStatus

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']