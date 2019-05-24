from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import validates

from core.sqlalchemy import db

class Provider(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key = True)
	rif = Column(VARCHAR(16))
	provider_status_id = Column(TINYINT(4), db.ForeignKey('provider_status.id'))
	provider_reputation_id = Column(TINYINT(4, unsigned=True), db.ForeignKey('provider_reputation.id'))
	name = Column(VARCHAR(256))
	fiscal_address = Column(VARCHAR(256))
	phone = Column(VARCHAR(16))
	city = Column(VARCHAR(256))
	state = Column(VARCHAR(256))
	creation_date = Column(TIMESTAMP())

	provider_status = db.relationship('ProviderStatus')
	provider_type = db.relationship('ProviderReputation')


class ProviderStatus(db.Model):
	id = Column(TINYINT(4), primary_key=True)
	code = Column(VARCHAR(16), nullable=False)
	description = Column(VARCHAR(64), nullable=False)

class ProviderReputation(db.Model):
	id = Column(TINYINT(4, unsigned=True), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(64))