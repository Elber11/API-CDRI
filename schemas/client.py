from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.client import Client as ModelClient
from models.client import ClientStatus as ModelClientStatus
from models.client import ClientType as ModelClientType

class Client(BaseSchemas):
	__model__ = ModelClient

	id = fields.Integer()
	cedula = fields.String(requiered=True)
	client_status_id = fields.Integer(requiered=True, load_only=True)
	client_status = fields.Nested('ClientStatus', data_key='client_status_id', dump_only=True)
	client_type_id = fields.Integer(requiered=True, load_only=True)
	client_type = fields.Nested('ClientType', data_key='client_type_id', dump_only=True)
	name = fields.String(requiered=True)
	last_name =fields.String(allow_none=True)
	address = fields.String(requiered=True)
	email = fields.String(allow_none=True)
	phone = fields.String(allow_none=True)
	creation_date = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)

	__filtering__ = ['id', 'name', 'last_name', 'cedula', 'phone', 'email', 'client_type_id', 'client_status_id', 'address']


class ClientStatus(BaseSchemas):
	__model__ = ModelClientStatus

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']

class ClientType(BaseSchemas):
	__model__ = ModelClientType

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']	