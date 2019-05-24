from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import validates

from core.sqlalchemy import db

class User(db.Model):
	id = Column(BIGINT(unsigned=True), primary_key=True)
	name = Column(VARCHAR(256))
	password = Column(VARCHAR(256))
	user_level_id = Column(TINYINT(unsigned=True), db.ForeignKey('user_level.id'))
	user_status_id = Column(TINYINT(), db.ForeignKey('user_status.id'))
	creation_date = Column(TIMESTAMP())

	user_level = db.relationship('UserLevel')
	user_status = db.relationship('UserStatus')

class UserLevel(db.Model):
	id = Column(TINYINT(unsigned=True), primary_key=True)
	code = Column(VARCHAR(16))
	description = Column(VARCHAR(64))

class UserStatus(db.Model):
	id = Column(TINYINT(), primary_key=True)
	code = Column(VARCHAR(16), nullable=False)
	description = Column(VARCHAR(64), nullable=False)	