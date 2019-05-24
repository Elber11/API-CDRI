from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import validates

from core.sqlalchemy import db

class Product(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key=True)
	name = Column(VARCHAR(256))
	product_category_id = Column(SMALLINT(5, unsigned=True), db.ForeignKey('product_category.id'))
	product_status_id = Column(TINYINT(4), db.ForeignKey('product_status.id'))
	product_commercial_brand_id = Column(SMALLINT(5, unsigned=True), db.ForeignKey('product_commercial_brand.id'))
	model = Column(VARCHAR(64))
	existence = Column(INTEGER(10, unsigned=True))
	price =  Column(FLOAT())

	product_category = db.relationship('ProductCategory')
	product_status = db.relationship('ProductStatus')
	product_commercial_brand = db.relationship('ProductCommercialBrand')

class ProductCategory(db.Model):
	id = Column(SMALLINT(5, unsigned=True), primary_key=True)
	name = Column(VARCHAR(128))
	creation_date = Column(TIMESTAMP())

class ProductStatus(db.Model):
	id = Column(TINYINT(4, unsigned=True), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(64))

class ProductCommercialBrand(db.Model):
	id = Column(SMALLINT(5, unsigned=True), primary_key=True)
	name = Column(VARCHAR(128))
	creation_date = Column(TIMESTAMP())