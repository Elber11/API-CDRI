from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import validates

from models.product import Product
from models.provider import Provider

from core.sqlalchemy import db

class InventoryFlow(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key = True)
	inventory_flow_type_id = Column(TINYINT(4, unsigned=True), db.ForeignKey('inventory_flow_type.id'))
	provider_id = Column(BIGINT(20, unsigned=True), db.ForeignKey('provider.id'))
	product_id = Column(BIGINT(20, unsigned=True), db.ForeignKey('product.id'))
	quantity = Column(INTEGER(11, unsigned=True))
	unity_price = Column(FLOAT())
	total_price = Column(FLOAT())
	datetime = Column(TIMESTAMP())

	inventory_flow_type = db.relationship('InventoryFlowType')
	product = db.relationship(Product)
	provider = db.relationship(Provider)

class InventoryFlowType(db.Model):
	id = Column(TINYINT(4), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(32))