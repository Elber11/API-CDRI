from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.provider import Provider as ModelProvider
from models.provider import ProviderStatus as ModelProviderStatus
from models.provider import ProviderReputation as ModelProviderReputation

class Provider(BaseSchemas):
	__model__ = ModelProvider

	id = fields.Integer()
	rif = fields.String(requiered=True)
	provider_reputation_id = fields.Integer(requiered=True, load_only=True)
	provider_reputation = fields.Nested('ProviderReputation', data_key='provider_reputation_id', dump_only=True)
	provider_status_id = fields.Integer(requiered=True, load_only=True)
	provider_status = fields.Nested('ProviderStatus', data_key='provider_status_id', dump_only=True)
	name = fields.String(requiered=True)
	fiscal_address = fields.String(requiered=True)
	phone = fields.String(requiered=True)
	state = fields.String(requiered=True)
	city = fields.String(requiered=True)
	creation_date = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)

	__filtering__ = ['id','rif', 'name', 'provider_reputation_id', 'provider_status_id', 'fiscal_address', 'phone', 'state', 'city']


class ProviderStatus(BaseSchemas):
	__model__ = ModelProviderStatus

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']

class ProviderReputation(BaseSchemas):
	__model__ = ModelProviderReputation

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']	