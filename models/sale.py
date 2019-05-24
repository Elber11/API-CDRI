from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import validates

from models.user import User
from models.client import Client

from core.sqlalchemy import db

class Sale(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key = True)
	user_id = Column(SMALLINT(5, unsigned=True), db.ForeignKey('user.id'))
	client_id = Column(BIGINT(20, unsigned=True), db.ForeignKey('client.id'))
	sale_status_id = Column(TINYINT(4), db.ForeignKey('sale_status.id'))
	creation_date = Column(TIMESTAMP())

	user = db.relationship(User)
	client = db.relationship(Client)
	sale_status = db.relationship('SaleStatus')
	
class SaleStatus(db.Model):
	id = Column(TINYINT(4), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(64))