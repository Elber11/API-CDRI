from marshmallow import fields
from marshmallow import validates
from marshmallow import ValidationError

from core.schemas_core import BaseSchemas
from models.user import User as ModelUser
from models.user import UserLevel as ModelUserLevel
from models.user import UserStatus as ModelUserStatus

class User(BaseSchemas):
	__model__ = ModelUser

	id = fields.Integer()
	name = fields.String(required=True, error_messages={'required': 'El nombre es requerido', 'null' : 'El nombre no puede estar vacío'})
	password = fields.String(required=True)
	user_level_id = fields.Integer(required=True, load_only=True)
	user_level = fields.Nested('UserLevel', data_key='user_level_id', dump_only=True)
	user_status_id = fields.Integer(required=True, load_only=True)
	user_status = fields.Nested('UserStatus', data_key='user_status_id', dump_only=True)
	creation = fields.DateTime(format='%d/%m/%Y %I:%M:%S %p', dump_only=True)
	
	__filtering__ = ['id', 'name', 'password','user_level_id', 'user_status_id']

class UserLevel(BaseSchemas):
	__model__ = ModelUserLevel
	
	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']

class UserStatus(BaseSchemas):
	__model__ = ModelUserStatus

	id = fields.Integer()
	code = fields.String(required=True)
	description = fields.String(required=True)

	__filtering__ = ['id', 'code', 'description']