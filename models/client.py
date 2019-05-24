from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import validates

from core.sqlalchemy import db

class Client(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key = True)
	cedula = Column(VARCHAR(8))
	client_status_id = Column(TINYINT(4), db.ForeignKey('client_status.id'))
	client_type_id = Column(TINYINT(4, unsigned=True), db.ForeignKey('client_type.id'))
	name = Column(VARCHAR(256))
	last_name = Column(VARCHAR(256))
	address = Column(VARCHAR(256))
	email = Column(VARCHAR(256))
	phone = Column(VARCHAR(16))
	creation_date = Column(TIMESTAMP())

	client_status = db.relationship('ClientStatus')
	client_type = db.relationship('ClientType')


class ClientStatus(db.Model):
	id = Column(TINYINT(4), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(32))

class ClientType(db.Model):
	id = Column(TINYINT(4, unsigned=True), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(128))