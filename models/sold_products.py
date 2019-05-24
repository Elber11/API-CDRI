from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import FLOAT

from models.sale import Sale
from models.product import Product

from sqlalchemy.orm import validates

from core.sqlalchemy import db

class SoldProducts(db.Model):
	sale_id = Column(BIGINT(20, unsigned=True), db.ForeignKey('sale.id'), primary_key=True)
	product_id = Column(BIGINT(20, unsigned=True), db.ForeignKey('product.id'), primary_key=True)
	quantity = Column(SMALLINT(6))
	unity_price = Column(FLOAT())
	total_price = Column(FLOAT())

	sale = db.relationship(Sale)
	product = db.relationship(Product)